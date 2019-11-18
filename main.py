import pandas as pd

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

print(new_tweets)
# load.inserir(new_tweets)

