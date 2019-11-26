import pandas as pd
import nltk
from string import punctuation
from nltk import tokenize
import unidecode
from sklearn.naive_bayes import MultinomialNB
import ast
from pymongo import MongoClient
import json
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from transformacoes import pre_processamento
from transformacoes import predicoes
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

def monta_dataframe(all_tweets):
    tweet_dict={}
    tweet_array_string=[]
    tweet_array=[]
    def quebrar():
        for tweet in all_tweets:
            if len(tweet["pilares"])>1:
                tweet_dict["id"] = tweet["id"]
                tweet_dict["full_text"]=tweet["full_text"]
                tweet_dict["created_at"]=tweet["created_at"]
                tweet_dict["sentimento"]=tweet["sentimento"]
                tweet_dict["pilares"]=tweet["pilares"][(len(tweet["pilares"])-1)]
                tweet["pilares"].pop()
                tweet_array_string.append(json.dumps(tweet_dict))
    i=0
    while (i < 8):
        quebrar()
        i=i+1

    for tweet in all_tweets:
        if type(tweet["pilares"]) == list:
            tweet["pilares"]=tweet["pilares"][len(tweet["pilares"])-1]

    for string in tweet_array_string:
        dicionario = ast.literal_eval(string)
        tweet_array.append(dicionario)  

    all_tweets.extend(tweet_array)

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
    # if len(dicionario['pilares'])==0:
    #     dicionario['pilares']='7'
        dataset = pd.DataFrame(all_tweets)
        dataset.drop('_id',inplace=True, axis=1)

        return dataset
def monta_dataframe_treino():
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
    dataset = pd.DataFrame(all_tweets)
    dataset.drop('_id',inplace=True, axis=1)
    return all_tweets

def random_forest(treino,teste, texto, classificacao):
    x_treino = predicoes.vectorizer(treino,texto)
    y_treino = treino[classificacao]
    x_teste = predicoes.vectorizer(teste,texto)
    y_teste = teste[classificacao]

    modelo = RandomForestClassifier(n_estimators=100)
    modelo.fit(x_treino, treino[classificacao])
    previsao_teste = modelo.predict(x_teste)
    print(classificacao, 'accuracy: ',accuracy_score(y_teste, previsao_teste))
    print(classificacao, 'f1: ',f1_score(y_teste, previsao_teste, average='weighted'))

client = MongoClient("mongodb+srv://leonardocroda:HLF2YMd3f1hf5cdo@classificar-tweets-srtwi.mongodb.net/admin?retryWrites=true&w=majority") # conecta num cliente do MongoDB rodando na sua máquina
db = client['classificar_tweets'] # acessa o banco de dados
collection = db['tweets'] # acessa a minha coleção dentro desse banco de dados
all_tweets=[]
all_tweets = list(collection.find({'pilares':{'$ne':'7'}} , {"id": 1,"full_text": 1,"sentimento": 1,"pilares": 1,"created_at":1}))

dataframe = monta_dataframe(all_tweets)
dataframe = pre_processamento.execute(dataframe,'full_text')
treino = monta_dataframe_treino()
treino = pre_processamento.execute(treino,'full_text')

print(dataframe)
print(treino)

# pilares = ['economia','pessoas','governos','mobilidade','ambiente','vida']
# for pilar in pilares:
#     random_forest(treino, dataframe, 'stopwords',pilar)


