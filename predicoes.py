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
  vetorizar = TfidfVectorizer(lowercase = False, max_features=50) 
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

  
def regressao_logistica(dataset, texto, classificacao):
  bag_of_words= vectorizer(dataset,texto)
  modelo = LogisticRegression(solver = 'lbfgs')
  modelo.fit(bag_of_words,dataset[classificacao])
  return modelo



# def naive_bayes(dataset, texto, classificacao):
#   #vetoriza o texto (bag of words)
#   x_treino, x_teste, y_treino, y_teste = vectorizer(dataset,texto,classificacao)

#   #treina e testa com naive bayes 
#   modelo =MultinomialNB()
#   modelo.fit(x_treino, y_treino)
#   return modelo

# def adaboost(dataset, texto, classificacao):
#   x_treino, x_teste, y_treino, y_teste = vectorizer(dataset,texto,classificacao)
#   modelo = AdaBoostClassifier(n_estimators=50, learning_rate=1)
#   modelo.fit(x_treino, y_treino)
#   previsao_teste = modelo.predict(x_teste)

#   return modelo.score(x_teste, y_teste)

# def decision_tree(dataset, texto, classificacao):
#   x_treino, x_teste, y_treino, y_teste = vectorizer(dataset,texto,classificacao)
#   modelo = DecisionTreeClassifier()
#   modelo.fit(x_treino, y_treino)
#   previsao_teste = modelo.predict(x_teste)

#   return modelo.score(x_teste, y_teste)

# def gradient(dataset, texto, classificacao):
#   x_treino, x_teste, y_treino, y_teste = vectorizer(dataset,texto,classificacao)
#   modelo = GradientBoostingClassifier()
#   modelo.fit(x_treino, y_treino)
#   previsao_teste = modelo.predict(x_teste)

#   return modelo.score(x_teste, y_teste)
# def svc(dataset, texto, classificacao):
#   x_treino, x_teste, y_treino, y_teste = vectorizer(dataset,texto,classificacao)
#   modelo = SVC()
#   modelo.fit(x_treino, y_treino)
#   previsao_teste = modelo.predict(x_teste)

#   return modelo.score(x_teste, y_teste)
# def random_forest(dataset, texto, classificacao):
#   x_treino, x_teste, y_treino, y_teste = vectorizer(dataset,texto,classificacao)
#   modelo = RandomForestClassifier()
#   modelo.fit(x_treino, y_treino)
#   previsao_teste = modelo.predict(x_teste)

#   return modelo.score(x_teste, y_teste)
# def mlp(dataset, texto, classificacao):
#   x_treino, x_teste, y_treino, y_teste = vectorizer(dataset,texto,classificacao)
#   modelo = MLPClassifier()
#   modelo.fit(x_treino, y_treino)
#   previsao_teste = modelo.predict(x_teste)

#   return modelo.score(x_teste, y_teste)

# def perceptron(dataset, texto, classificacao):
#   x_treino, x_teste, y_treino, y_teste = vectorizer(dataset,texto,classificacao)
#   modelo = Perceptron()
#   modelo.fit(x_treino, y_treino)
#   previsao_teste = modelo.predict(x_teste)
#   return modelo.score(x_teste, y_teste)
  
# def knn(dataset, texto, classificacao):
#   #vetoriza o texto (bag of words)
#   x_treino, x_teste, y_treino, y_teste = vectorizer(dataset,texto,classificacao)

#   #treina e testa com KNN
#   modelo = KNeighborsClassifier()
#   modelo.fit(x_treino, y_treino)
#   previsao_teste = modelo.predict(x_teste)

#   return modelo.score(x_teste, y_teste)
#   f1_score(y_teste, previsao_teste, average='weighted')