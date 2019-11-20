import nltk
from nltk import tokenize
from string import punctuation
import unidecode
import pandas as pd
import re

def execute(dataframe, coluna_texto):
  def remove_links(dataframe,coluna_texto):
    frase_processada = list()
    for tweet in dataframe[coluna_texto]:
      tweet_processado= re.sub(r"http\S+", "", tweet)
      frase_processada.append(tweet_processado)
    return frase_processada
  dataframe['sem_links']= remove_links(dataframe,coluna_texto)

  def remove_pontuacao(dataframe,coluna_texto):
    token_pontuacao = tokenize.WordPunctTokenizer()
    pontuacao = list()
    for ponto in punctuation:
      pontuacao.append(ponto)
    
    frase_processada = list()
    for tweet in dataframe[coluna_texto]:
      nova_frase = list()
      palavras_texto = token_pontuacao.tokenize(tweet)
      for palavra in palavras_texto:
          if palavra not in pontuacao:
            nova_frase.append(palavra)
      frase_processada.append(' '.join(nova_frase))
    return frase_processada

  dataframe["sem_pontuacao"]=remove_pontuacao(dataframe,'sem_links')


  def remove_acentos(dataframe,coluna_texto):
    sem_acentos = [unidecode.unidecode(tweet) for tweet in dataframe[coluna_texto]]
    return sem_acentos
  dataframe['sem_acentos']=remove_acentos(dataframe,'sem_pontuacao')

  # def lowercase(dataframe, coluna_texto):
  #   minusculos = list()
  #   for tweet in dataframe[coluna_texto]:
  #     minusculos.append(tweet.lower())
  #   return minusculos
  # dataframe['lowercase']=lowercase(dataframe,'sem_acentos')

  # def remove_stopwords(dataframe, coluna_texto):
  #   nltk.download('stopwords')
  #   #removendo stopwords
  #   palavras_irrelevantes = nltk.corpus.stopwords.words("portuguese")
  #   palavras_irrelevantes.extend(['...','rt','"',"'",'.'])
  #   frase_processada = list()
  #   token_espaco = nltk.tokenize.WhitespaceTokenizer()

  #   for tweet in dataframe[coluna_texto]:
  #       nova_frase = list()
  #       palavras_texto = token_espaco.tokenize(tweet)
        
  #       for palavra in palavras_texto:
  #           if palavra not in palavras_irrelevantes:
  #               nova_frase.append(palavra)
  #       frase_processada.append(' '.join(nova_frase))

  #   return frase_processada
  # dataframe["stopwords"]=remove_stopwords(dataframe,'lowercase')

  def stemmer(dataframe, coluna_texto):
    token_pontuacao = tokenize.WordPunctTokenizer()
    nltk.download('rslp')
    stemmer = nltk.RSLPStemmer()
    #faz o stemmer
    frase_processada = list()
    for tweet in dataframe[coluna_texto]:
      nova_frase = list()
      palavras_texto = token_pontuacao.tokenize(tweet)
      for palavra in palavras_texto:
        nova_frase.append(stemmer.stem(palavra))
      frase_processada.append(' '.join(nova_frase))
    return frase_processada  
  dataframe["stemmer"] = stemmer(dataframe,'sem_acentos')
  return dataframe
