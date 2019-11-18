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
from transformacoes.buscar_tweets import buscar_tweets
from transformacoes import predicoes
from transformacoes import novos_tweets
from extracao import minas
from carga import load

dataframe = buscar_tweets()
dataframe = pre_processamento.execute(dataframe,'full_text')
minas = minas.minas()
minas = pre_processamento.execute(minas,'full_text')
modelo_sentimento = predicoes.naive_bayes(minas, 'stopwords','sentimento')

new_tweets = novos_tweets.buscar_novos_tweets()
new_tweets = pre_processamento.execute(new_tweets, 'full_text')

pilares = ['economia','pessoas','governos','mobilidade','ambiente','vida']
for pilar in pilares:
    print('... Processing {}'.format(pilar))
    modelo = predicoes.random_forest(dataframe,'stopwords',pilar)
    new_tweets = novos_tweets.classificar(new_tweets, 'stopwords', pilar, modelo)

new_tweets = novos_tweets.classificar(new_tweets,'stopwords','sentimento',modelo_sentimento)

# load.inserir(new_tweets)

