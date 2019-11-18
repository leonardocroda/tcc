import pandas as pd
def minas():
    minas_raw = pd.read_csv("https://raw.githubusercontent.com/minerandodados/mdrepo/master/Tweets_Mg.csv")
    minas = pd.DataFrame()
    minas["full_text"]=minas_raw['Text']
    sentimento = minas_raw["Classificacao"].replace(["Negativo", "Positivo","Neutro"],[0, 1, 2])
    minas['sentimento']=sentimento
    minas['created_at']=minas_raw['Created At']

    return minas