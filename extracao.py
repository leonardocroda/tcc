from pymongo import MongoClient
import tweepy
import json

def extrair():
  # CONFIGURAÇÃO DA API DO TWITTER 
  consumer_key = 'rvY15wPTQqIS8FhW9up66IIa1'
  consumer_secret_key = 'ub6D0RdPIWbfzWnKsOi6BCjpMNTcC16kFhrKQRGKUPfNLYXskV'
  access_token = '610407857-gGrcIDCMg7CRAqCc7Wm2qhQlNmgZ6f3DZTNJ7ZVW'
  access_secret_token = 'ZCEXOixbsKKHKJBFiwJrpW7kB3C4eUhUTBgKsLcKeCFPm'
  authentication = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
  authentication.set_access_token(access_token, access_secret_token)
  twitter = tweepy.API(authentication)

  resultados = [] # Variável que recebe todos os tweets coletados

  # Obter os ultimos 20 mil tweets disponiveis com as palavras 'balneario camboriu'
  for tweet in tweepy.Cursor(twitter.search, q='balneario camboriu',  
  tweet_mode='extended').items(20000):
      resultados.append(tweet)

  # Verificando o numero de tweets coletados
  len(resultados)

  # Configuração de conexão com o MongoDB

  cliente = MongoClient()  # Iniciando o client do mongo
  banco = cliente.tweets_python # Conectando com o banco de dados
  tweets_collection = banco.tweets # Escolhendo a collection na qual os tweets serão inseridos

  resultados_json=[]

  for tweet in resultados:  # Transformando o dado que retorna da api do twitter (list) em json para inserir no mongo
    tweet_json = tweet._json # _json é a coluna da lista que possui todos os dados do tweet que preciso
    resultados_json.append(tweet_json) 
  tweets_collection.insert_many(resultados_json) # Inserindo os dados no banco

  print("foram inseridos " , len(resultados), " Tweets")