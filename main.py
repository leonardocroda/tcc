import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import nltk
from string import punctuation
from nltk import tokenize
import unidecode
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import f1_score
import ast
from pymongo import MongoClient
import json
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import Perceptron
from sklearn.model_selection import cross_validate

from transformacoes import pre_processamento
from transformacoes import construirDataframeTreino
from transformacoes import predicoes
from transformacoes import novos_tweets
from transformacoes import datas
from carga import load
all_tweets = construirDataframeTreino.buscar_tweets_mongo()
dataframe = construirDataframeTreino.monta_dataframe(all_tweets)
dataframe = pre_processamento.execute(dataframe,'full_text')
modelo_sentimento = predicoes.regressao_logistica(dataframe, 'stemmer','sentimento')
modelo_pilares = predicoes.regressao_logistica(dataframe, 'stemmer','pilares')
new_tweets = novos_tweets.buscar_novos_tweets()
new_tweets = pre_processamento.execute(new_tweets, 'full_text')
new_tweets = novos_tweets.classificar(new_tweets, 'stemmer', 'sentimento', modelo_sentimento)
new_tweets = novos_tweets.classificar(new_tweets, 'stemmer', 'pilares', modelo_pilares)
# print(predicoes.metricas(dataframe, 'stemmer', 'sentimento', LogisticRegression()))
load.inserir(new_tweets)
# print(new_tweets["sentimento"][1])
# print(datas.transformar(new_tweets["created_at"]))

