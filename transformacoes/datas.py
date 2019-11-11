def transformar(datas):
    datas_arr = list()
   
    for data in datas:
        data = data.split()
        data_dic=dict()
        data_dic["day"] = int(data[2])
        data_dic["month"] = data[1]
        data_dic["year"] = int(data[5])
        data_dic["dayweek"] = data[0]
        data_dic["hour"] = data[3]
        hora = data_dic["hour"].split(':')
        hora = int(hora[0])
        
        if(hora >= 18 or hora < 6):
            data_dic["shift"] = "night"
        elif(hora >= 6 and hora < 12):
            data_dic["shift"] = "morning"
        elif(hora >= 12 and hora < 18 ):
            data_dic["shift"] = "afternoon"
        else:
            data_dic["shift"]='ero'
        
        datas_arr.append(data_dic)
    return datas_arr

