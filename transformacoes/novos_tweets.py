from pymongo import MongoClient
import pandas as pd
from transformacoes import predicoes 
import json
import ast

def buscar_novos_tweets():
    client = MongoClient("mongodb+srv://leonardocroda:HLF2YMd3f1hf5cdo@classificar-tweets-srtwi.mongodb.net/admin?retryWrites=true&w=majority") # conecta num cliente do MongoDB rodando na sua máquina
    db = client['classificar_tweets'] # acessa o banco de dados
    collection = db['new_tweets'] # acessa a minha coleção dentro desse banco de dados
    new_tweets = list(collection.find({} , {"id":1,"full_text": 1, "created_at":1}))
    new_tweets=pd.DataFrame(new_tweets)
    new_tweets.drop('_id', inplace=True, axis=1)

    return new_tweets

def classificar(new_tweets, texto, classificacao, modelo):
    bag_of_words = predicoes.vectorizer(new_tweets,texto)
    predicao = modelo.predict(bag_of_words)
    new_tweets[classificacao]=predicao
    return new_tweets

def unir(new_tweets):
    lista =  new_tweets.values.tolist()
    lista_dicionarios=[]
    for item in lista:
        dicionario={}
        dicionario['created_at'] = item[0]
        dicionario['id']= item[1]
        dicionario['full_text']=item[2]
        dicionario['sem_links']=item[3]
        dicionario['sem_pontuacao']=item[4]
        dicionario['sem_acentos']=item[5]
        dicionario['stemmer']=item[6]
        dicionario['economia']=item[7]
        dicionario['pessoas']=item[8]
        dicionario['governos']=item[9]
        dicionario['mobilidade']=item[10]
        dicionario['ambiente']=item[11]
        dicionario['vida']=item[12]
        dicionario['sentimento']=item[13]
        dicionario['pilares']=[]
        if dicionario['economia']==1:
            dicionario['pilares'].extend('1')
       
        if dicionario['pessoas']==1:
            
            dicionario['pilares'].extend('2')
        
        
        if dicionario['governos']==1:
            
            dicionario['pilares'].extend('3')
        
        if dicionario['mobilidade']==1:
            
            dicionario['pilares'].extend('4')
        
        if dicionario['ambiente']==1:
            
            dicionario['pilares'].extend('5')
        
        if dicionario['vida']==1:
            
            dicionario['pilares'].extend('6')
        if len(dicionario['pilares'])==0:
            dicionario['pilares']='7'
        lista_dicionarios.append(dicionario)

    return lista_dicionarios

def quebra(all_tweets):
    tweet_dict={}
    tweet_array_string=[]
    tweet_array=[]
    # all_tweets=list(all_tweets)
    #caso o tweet tenha mais de um assunto, é atribuido ele é adicionado a tweet_dict e o ultimo assunto é removido da coluna 
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
    #executa quebrar 6 vezes, pois são 6 assuntos possíveis
    i=0
    while (i < 7):
        quebrar()
        i=i+1
    #quando eu removo os assuntos, no tweet original o tipo do dado continua sendo lista, isso atribui a pilares a string do pilar em si
    for tweet in all_tweets:
        if type(tweet["pilares"]) == list:
            tweet["pilares"]=tweet["pilares"][len(tweet["pilares"])-1]
  # não consegui fazer append do dicionario na lista, por isso transformei o dicionario 
  #em string, esse bloco transforma eles em dicionario novamente, isso é necessário para transformar em dataframe
    for string in tweet_array_string:
        dicionario = ast.literal_eval(string)
        tweet_array.append(dicionario)  
  #junta a lista original com a dos tweets q tinham mais de um assunto
    all_tweets.extend(tweet_array)

    dataset = pd.DataFrame(all_tweets)
    return dataset