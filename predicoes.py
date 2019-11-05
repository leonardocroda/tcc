from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import pandas as pd

dataframe=pd.DataFrame()

def vectorizer(dataset,texto,classificacao):
  vetorizar = TfidfVectorizer(lowercase = False, max_features=50)
  bag_of_words = vetorizar.fit_transform(dataset[texto])
  divisoes= train_test_split(bag_of_words, dataset[classificacao], random_state = 42)
  return divisoes

def logistic_regression(dataset, texto, classificacao):
  x_treino, x_teste, y_treino, y_teste = vectorizer(dataset,texto,classificacao)

  modelo = LogisticRegression(solver="lbfgs", multi_class="multinomial")
  modelo.fit(x_treino, y_treino)
  previsao_teste = modelo.predict(x_teste)
  print(confusion_matrix(y_teste, previsao_teste))
  print(confusion_matrix(y_teste, previsao_teste).ravel())
  

  return modelo.score(x_teste, y_teste)

def naive_bayes(dataset, texto, classificacao):
  #vetoriza o texto (bag of words)
  x_treino, x_teste, y_treino, y_teste = vectorizer(dataset,texto,classificacao)

  #treina e testa com naive bayes 
  modelo =MultinomialNB()
  modelo.fit(x_treino, y_treino)
  return modelo.score(x_teste, y_teste)




def knn(dataset, texto, classificacao):
  #vetoriza o texto (bag of words)
  x_treino, x_teste, y_treino, y_teste = vectorizer(dataset,texto,classificacao)

  #treina e testa com KNN
  modelo = KNeighborsClassifier()
  modelo.fit(x_treino, y_treino)
  return modelo.score(x_teste, y_teste)

print("Acurácia da Regressão Logística: " , logistic_regression(dataframe, "stemmer", "poder_publico"))
print("Acurácia do Naive-Bayes: " , naive_bayes(dataframe, "stemmer", "populacao"))
print("Acurácia do KNN: " , knn(dataframe, "stemmer", "populacao"))