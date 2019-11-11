from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_validate
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import Perceptron
import ast
import pandas as pd

def vectorizer(dataset,texto):
  vetorizar = TfidfVectorizer(lowercase = False, max_features=4750) 
  bag_of_words = vetorizar.fit_transform(dataset[texto])
  return bag_of_words

def metricas(dataset, texto, classificacao, modelo):
  bag_of_words = vectorizer(dataset,texto)
  return cross_validate(modelo, bag_of_words, dataset[classificacao], return_train_score=False,
               scoring=['accuracy',
                        'average_precision',
                        'f1',
                        'precision',
                        'recall',
                        'roc_auc'],cv=10)

def decision_tree(dataset, texto, classificacao):
  bag_of_words= vectorizer(dataset,texto)
  modelo = DecisionTreeClassifier()
  modelo.fit(bag_of_words,dataset[classificacao])
  return modelo

def random_forest(dataset, texto, classificacao):
  bag_of_words= vectorizer(dataset,texto)
  modelo = RandomForestClassifier()
  modelo.fit(bag_of_words,dataset[classificacao])
  return modelo

def naive_bayes(dataset, texto, classificacao):
  bag_of_words= vectorizer(dataset,texto)
  modelo = MultinomialNB()
  modelo.fit(bag_of_words,dataset[classificacao])
  return modelo

def perceptron(dataset, texto, classificacao):
  bag_of_words= vectorizer(dataset,texto)
  modelo = Perceptron()
  modelo.fit(bag_of_words,dataset[classificacao])
  return modelo  

def svc(dataset, texto, classificacao):
  bag_of_words= vectorizer(dataset,texto)
  modelo = SVC()
  modelo.fit(bag_of_words,dataset[classificacao])
  return modelo
  
def knn(dataset, texto, classificacao):
  bag_of_words= vectorizer(dataset,texto)
  modelo = KNeighborsClassifier()
  modelo.fit(bag_of_words,dataset[classificacao])
  return modelo

def regressao_logistica(dataset, texto, classificacao):
  bag_of_words= vectorizer(dataset,texto)
  modelo = LogisticRegression(solver = 'lbfgs')
  modelo.fit(bag_of_words,dataset[classificacao])
  return modelo

def gradient(dataset, texto, classificacao):
  bag_of_words= vectorizer(dataset,texto)
  modelo = GradientBoostingClassifier()
  modelo.fit(bag_of_words,dataset[classificacao])
  return modelo  