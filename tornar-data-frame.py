from pymongo import MongoClient
import json
import ast
import pandas as pd

#CONEXÃO COM O MONGO
client = MongoClient("mongodb+srv://leonardocroda:HLF2YMd3f1hf5cdo@classificar-tweets-srtwi.mongodb.net/admin?retryWrites=true&w=majority") # conecta num cliente do MongoDB rodando na sua máquina
db = client['classificar_tweets'] # acessa o banco de dados
collection = db['teste'] # acessa a minha coleção dentro desse banco de dados

# Atribuindo as propriedades id, full_text, sentimento e pilares do BD a uma lista Python
all_tweets = list(collection.find({},{"id": 1,"full_text": 1,"sentimento": 1,"pilares": 1}))

#Variáveis de apoio
tweet_dict={}
tweet_array_string=[]
tweet_array=[]

# Quebrando tweets que possuam mais de um pilar em vários tweets (um por pilar)
def quebrar():
  for tweet in all_tweets:
    if len(tweet["pilares"])>1:
      tweet_dict["id"] = tweet["id"]
      tweet_dict["full_text"]=tweet["full_text"]
      tweet_dict["sentimento"]=tweet["sentimento"]
      tweet_dict["pilares"]=tweet["pilares"][(len(tweet["pilares"])-1)]
      tweet["pilares"].pop()
      tweet_array_string.append(json.dumps(tweet_dict))
i=0
while(i < 8):
  quebrar()
  i=i+1
# Transformando as listas que sobraram na coluna pilares em String
for tweet in all_tweets:
  if type(tweet["pilares"]) == list:
    tweet["pilares"]=tweet["pilares"][len(tweet["pilares"])-1]

# Transformando os elementos q foram "appendizados" como string em dicionarios e atribuindo a lista tweet_array
for string in tweet_array_string:
  dicionario = ast.literal_eval(string)
  tweet_array.append(dicionario)   

# Juntando a lista all_tweets com a tweet_array
all_tweets.extend(tweet_array)

# Transformando all_tweets em um DataFrame do Pandas
import pandas as pd
df = pd.DataFrame(all_tweets)
print(df)