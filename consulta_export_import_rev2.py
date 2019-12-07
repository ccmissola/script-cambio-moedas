'''
Utilizamos a função get do requests para acessar o servidor da API onde se encontra as informações das moedas.
Ao acessar o servidor, a variável status_code, do requests, é preenchida com a resposta HTTP do servidor. Ea variável content, também do requests,
é preenchida com o conteúdo da API (JSON)
Utilizamos a biblioteca json, para converter os dados recebidos, em um dicionário.
''' 
import requests
import json
import pandas

def converter_data(dia):
    dia = dia[8:]+'/'+dia[5:7]+'/'+dia[0:4] 
    print('Ultima atualização dos dados: ', dia)
    return dia   

def chave_acesso(chave='4d4a3319e18c4826122ed3f62d8ee691&format=1'):
    return "http://data.fixer.io/api/latest?access_key="+chave

def converter_em_reais (valor_real, valor_estrangeiro):
    return round (valor_real/valor_estrangeiro, 2)    

def exportar_tabela (lista_titulos, lista_valores, nome_arquivo, lista_dia):
    celulas = pandas.DataFrame({'Moedas':lista_titulos, 'Valores':lista_valores,'Acessado em':lista_dia})
    celulas.to_csv(nome_arquivo+'.csv',index=False)
    print('Tabela exportada com sucesso')

def main():
    chave = input('Informe a chave de acesso do Fixer.io, se não tiver, aperte enter: ')
    url = chave_acesso(chave) if len (chave) > 0 else chave_acesso()
    print ('Acessando base de dados...')
    resposta = requests.get(url)
    print(resposta)
    if resposta.status_code == 200:
        print('Conexão com a base de dados, estabeleciada com sucesso...')
        dados = resposta.json()
        #A função converter data irá receber o valor da variável dados['date'] e irá retornar a data convertida no padrão Brasil
        # que será atribuída a variável dia_convertido
        dia_convertido = converter_data(dados['date'])
        print(dados['rates']['BTC'], 'Bitcoin')
        print(dados['rates']['EUR'], 'Euro')
        print(dados['rates']['BRL'], 'Real')
        print(dados['rates']['USD'], 'Dolar')
        euro_em_reais = converter_em_reais (dados['rates']['BRL'], dados['rates']['EUR'])
        bitcoin_em_reais = converter_em_reais(dados['rates']['BRL'], dados['rates']['BTC'])
        dollar_em_reais = converter_em_reais (dados ['rates']['BRL'], dados['rates']['USD'])
        escolha = input('Digite: \nB - Bitcoin\nD - Dollar\nE - Euro\nA- Todas: ').upper()
        if (escolha == 'B'):
            exportar_tabela(['Bitcoin'], [bitcoin_em_reais], 'Bitcoin', [dia_convertido])
        elif (escolha == 'D'):
            exportar_tabela(['Dollar'],[dollar_em_reais], 'Dollar', [dia_convertido])
        elif (escolha == 'E'):
            exportar_tabela(['Euro'],[euro_em_reais], 'Euro', [dia_convertido])
        elif (escolha == 'A'):
            exportar_tabela(['Bitcoin', 'Dollar', 'Euro'],[bitcoin_em_reais, dollar_em_reais, euro_em_reais], 'moedas', [dia_convertido, '',''])
        else:
            print('Você não escolheu nenhuma das opções. Sua tabela não será exportada!')
    

    else:
        print('Erro ao acessar a base de dados')

if __name__ == '__main__':
    main()

