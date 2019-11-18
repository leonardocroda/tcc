from pymongo import MongoClient
import pandas as pd

def buscar_tweets():
  client = MongoClient("mongodb+srv://leonardocroda:HLF2YMd3f1hf5cdo@classificar-tweets-srtwi.mongodb.net/admin?retryWrites=true&w=majority") # conecta num cliente do MongoDB rodando na sua máquina
  db = client['classificar_tweets'] # acessa o banco de dados
  collection = db['dataset'] # acessa a minha coleção dentro desse banco de dados
  all_tweets=[]
  all_tweets = list(collection.find({} , {"id": 1,"full_text": 1,"pilares": 1,"created_at":1}))

  for tweet in all_tweets:
    if(tweet['pilares']=='1'):
      tweet['economia']=1
    else:
      tweet['economia']=0  
    
    if(tweet['pilares']=='2'):
      tweet['pessoas']=1
    else:
      tweet['pessoas']=0
    
    if(tweet['pilares']=='3'):
      tweet['governos']=1
    else:
      tweet['governos']=0
    
    if(tweet['pilares']=='4'):
      tweet['mobilidade']=1
    else:
      tweet['mobilidade']=0
  
    if(tweet['pilares']=='5'):
      tweet['ambiente']=1
    else:
      tweet['ambiente']=0
  
    if(tweet['pilares']=='6'):
      tweet['vida']=1
    else:
      tweet['vida']=0
    
  dataframe = pd.DataFrame(all_tweets)
  dataframe.drop('_id', inplace=True, axis=1)
  
  return dataframe