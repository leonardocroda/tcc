import pandas as pd
def minas():
    minas_raw = pd.read_csv("https://raw.githubusercontent.com/minerandodados/mdrepo/master/Tweets_Mg.csv")
    minas = pd.DataFrame()
    minas["full_text"]=minas_raw['Text']
    sentimento = minas_raw["Classificacao"].replace(["Negativo", "Positivo","Neutro"],[0, 1, 2])
    minas['sentimento']=sentimento
    minas['created_at']=minas_raw['Created At']
    # i=200000
    # minas_dics=[]
    # minas = minas.values.tolist()
    # for item in minas:
    #     minas_dic={}
    #     minas_dic['created_at']=item[4]
    #     minas_dic['id']=i
    #     minas_dic['full_text']=item[0]
    #     minas_dic['sentimento']=item[1]
    #     minas_dic['_id']=item[3]
    #     minas_dics.append(minas_dic)
    #     i=i+2
    return minas