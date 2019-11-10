from pymongo import MongoClient
import pandas as pd
from predicoes import vectorizer
def buscar_novos_tweets():
    client = MongoClient("mongodb+srv://leonardocroda:HLF2YMd3f1hf5cdo@classificar-tweets-srtwi.mongodb.net/admin?retryWrites=true&w=majority") # conecta num cliente do MongoDB rodando na sua máquina
    db = client['classificar_tweets'] # acessa o banco de dados
    collection = db['new_tweets'] # acessa a minha coleção dentro desse banco de dados
    new_tweets = list(collection.find({} , {"id":1,"full_text": 1}))
    new_tweets=pd.DataFrame(new_tweets)
    return new_tweets

def classificar(new_tweets, texto, classificacao, modelo):
    bag_of_words = vectorizer(new_tweets,texto)
    predicao = modelo.predict(bag_of_words)
    new_tweets[classificacao]=predicao
    return new_tweets

