'''
Utilizamos a função get do requests para acessar o servidor da API onde se encontra as informações das moedas.
Ao acessar o servidor, a variável status_code, do requests, é preenchida com a resposta HTTP do servidor. Ea variável content, também do requests,
é preenchida com o conteúdo da API (JSON)
Utilizamos a biblioteca json, para converter os dados recebidos, em um dicionário.
''' 
import requests
import json
url = 'http://data.fixer.io/api/latest?access_key=4d4a3319e18c4826122ed3f62d8ee691&format=1'
print ('Acessando base de dados...')
resposta = requests.get(url)
print(resposta)
if resposta.status_code == 200:
    print('Conexão com a base de dados, estabeleciada com sucesso...')
    dados = resposta.json()
    dia = dados ['date']
    dia = dia[8:]+'/'+dia[5:7]+'/'+dia[0:4]
    print('Ultima atualização dos dados: ', dia)
    print(dados['rates']['BTC'], 'Bitcoin')
    print(dados['rates']['EUR'], 'Euro')
    print(dados['rates']['BRL'], 'Real')
    euro_em_reais = round (dados['rates']['BRL']/dados['rates']['EUR'],2)
    bitcoin_em_reais = round (dados['rates']['BRL']/dados['rates']['BTC'],2)
    print('1 Euro vale', euro_em_reais, 'reais')
    print('1 Bitcoin vale', bitcoin_em_reais, 'reais')

else:
    print('Erro ao acessar a base de dados')

