import psycopg2
from transformacoes import datas



def inserir(dataframe):
    ids = list(dataframe["id"])
    textos = list(dataframe["sem_acentos"])
    tempos = datas.transformar(dataframe["created_at"])
    
    con = psycopg2.connect(host='localhost', database='datawarehouse',
    user='postgres', password='metallum1')
    cur = con.cursor()
    i=0
    for texto in textos:
        id=ids[i]
        sql = "insert into dimtext(iddimtext,text) values (" + str(id) + ','+ "$string$"+ str(texto) + "$string$)"
        print(sql)
        print(i)
    #     cur.execute(sql)
        i=i+1
    # i=0
    # for data in tempos:
    #     id=ids[i]
    #     sql = "insert into dimtime(iddimtime,day,month,year,dayweek,hour,shift) values("+ str(id)+","+ str(data['day'])+",'"+data['month']+"',"+str(data['year'])+",'"+data['dayweek']+"','"+data['hour']+"','"+data['shift']+"')"
    #     cur.execute(sql)
    #     i=i+1
    # for tweet in dataframe.itertuples(index = True, name='Pandas'):
    #     # print(tweet)
    #     sql= "insert into facttweet(characteristics,feeling,text,time) values ('"+getattr(tweet,'pilares')+"',"+str(getattr(tweet,'sentimento'))+","+str(getattr(tweet,"id"))+","+str(getattr(tweet,"id"))+")"
    #     cur.execute(sql)
    # con.commit()
    # con.close()

