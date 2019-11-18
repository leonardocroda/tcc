from sklearn.pipeline import Pipeline
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.model_selection import cross_validate
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Perceptron
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier

def decision_tree_metrics(dataframe):
  categories = ['sentimento']
  # categories = ['economia','pessoas','governos','mobilidade','ambiente','vida']
  stop = nltk.corpus.stopwords.words("portuguese")
  pipeline = Pipeline([
                  ('tfidf', TfidfVectorizer(lowercase=True, ngram_range=(1,2), stop_words= stop)),
                  ('clf', OneVsRestClassifier(DecisionTreeClassifier(), n_jobs=1)),
              ])
  for category in categories:
      print('... Processing {}'.format(category))
      print('Validação Cruzada: \n', cross_validate(pipeline, dataframe.lowercase, dataframe[category],
                                                    scoring=['accuracy',
                                                              # 'f1',
                                                            ], cv=10),"\n")

def random_forest_metrics(dataframe):
  categories = ['economia','pessoas','governos','mobilidade','ambiente','vida']
  stop = nltk.corpus.stopwords.words("portuguese")
  pipeline = Pipeline([
                  ('tfidf', TfidfVectorizer(lowercase=True, ngram_range=(1,2), stop_words= stop)),
                  ('clf', OneVsRestClassifier(RandomForestClassifier(n_estimators=10), n_jobs=1)),
              ])
  for category in categories:
      print('... Processing {}'.format(category))
      print('Validação Cruzada: \n', cross_validate(pipeline, dataframe.lowercase, dataframe[category],
                                                    scoring=['accuracy',
                                                              'f1',
                                                            ], cv=10),"\n")
                                                            
def logistic_regression_metrics(dataframe):
  categories = ['economia','pessoas','governos','mobilidade','ambiente','vida']
  stop = nltk.corpus.stopwords.words("portuguese")
  pipeline = Pipeline([
                  ('tfidf', TfidfVectorizer(lowercase=True, ngram_range=(1,2), stop_words= stop)),
                  ('clf', OneVsRestClassifier(LogisticRegression(), n_jobs=1)),
              ])
  for category in categories:
      print('... Processing {}'.format(category))
      print('Validação Cruzada: \n', cross_validate(pipeline, dataframe.lowercase, dataframe[category],
                                                    scoring=['accuracy',
                                                              'f1',
                                                            ], cv=10),"\n")                      
                                                                                                
def naive_bayes_metrics(dataframe):
  categories = ['economia','pessoas','governos','mobilidade','ambiente','vida']
  stop = nltk.corpus.stopwords.words("portuguese")
  pipeline = Pipeline([
                  ('tfidf', TfidfVectorizer(lowercase=True, ngram_range=(1,2), stop_words= stop)),
                  ('clf', OneVsRestClassifier(MultinomialNB(), n_jobs=1)),
              ])
  for category in categories:
      print('... Processing {}'.format(category))
      print('Validação Cruzada: \n', cross_validate(pipeline, dataframe.lowercase, dataframe[category],
                                                    scoring=['accuracy',
                                                              'f1',
                                                            ], cv=10),"\n")        

def gradient_metrics(dataframe):
  categories = ['economia','pessoas','governos','mobilidade','ambiente','vida']
  stop = nltk.corpus.stopwords.words("portuguese")
  pipeline = Pipeline([
                  ('tfidf', TfidfVectorizer(lowercase=True, ngram_range=(1,2), stop_words= stop)),
                  ('clf', OneVsRestClassifier(GradientBoostingClassifier(), n_jobs=1)),
              ])
  for category in categories:
      print('... Processing {}'.format(category))
      print('Validação Cruzada: \n', cross_validate(pipeline, dataframe.lowercase, dataframe[category],
                                                    scoring=['accuracy',
                                                              'f1',
                                                            ], cv=10),"\n")  

def perceptron_metrics(dataframe):
  categories = ['economia','pessoas','governos','mobilidade','ambiente','vida']
  stop = nltk.corpus.stopwords.words("portuguese")
  pipeline = Pipeline([
                  ('tfidf', TfidfVectorizer(lowercase=True, ngram_range=(1,2), stop_words= stop)),
                  ('clf', OneVsRestClassifier(Perceptron(), n_jobs=1)),
              ])
  for category in categories:
      print('... Processing {}'.format(category))
      print('Validação Cruzada: \n', cross_validate(pipeline, dataframe.lowercase, dataframe[category],
                                                    scoring=['accuracy',
                                                              'f1',
                                                            ], cv=10),"\n")  


def vectorizer(dataset,texto):
  vetorizar = TfidfVectorizer(lowercase=True, ngram_range=(1,2), max_features=5000) 
  bag_of_words = vetorizar.fit_transform(dataset[texto])
  return bag_of_words

def decision_tree(dataset, texto, classificacao):
  bag_of_words = vectorizer(dataset,texto)
  modelo = DecisionTreeClassifier()
  modelo.fit(bag_of_words, dataset[classificacao])
  return modelo

def random_forest(dataset, texto, classificacao):
  bag_of_words = vectorizer(dataset,texto)
  modelo = RandomForestClassifier(n_estimators=10)
  modelo.fit(bag_of_words, dataset[classificacao])
  return modelo

def naive_bayes(dataset, texto, classificacao):
  bag_of_words = vectorizer(dataset,texto)
  modelo = MultinomialNB()
  modelo.fit(bag_of_words, dataset[classificacao])
  return modelo

def perceptron(dataset, texto, classificacao):
  bag_of_words = vectorizer(dataset,texto)
  modelo = Perceptron()
  modelo.fit(bag_of_words, dataset[classificacao])
  return modelo

 
def knn(dataset, texto, classificacao):
  bag_of_words = vectorizer(dataset,texto)
  modelo = KNeighborsClassifier()
  modelo.fit(bag_of_words, dataset[classificacao])
  return modelo

def regressao_logistica(dataset, texto, classificacao):
  bag_of_words = vectorizer(dataset,texto)
  modelo = LogisticRegression(solver='lbfgs')
  modelo.fit(bag_of_words, dataset[classificacao])
  return modelo

def gradient(dataset, texto, classificacao):
  bag_of_words = vectorizer(dataset,texto)
  modelo = GradientBoostingClassifier()
  modelo.fit(bag_of_words, dataset[classificacao])
  return modelo
