import pandas as pd

datos = pd.read_csv("baseClientesHackaton2022.csv")
df = pd.DataFrame(datos)
#print(df.head(5))

def permisoIntermedio(idCliente):
    df = pd.read_csv("./baseClientesHackaton2022.csv",index_col="idCliente",parse_dates=True)
    #idCliente = 'BF000002999'
    #try:
    df2 =df.loc[idCliente].tolist()
    print(df2)
    for c in range(12):
            #print(c)
        if(c==1) or (c==2) or (c==3) or (c==6) or (c==7) or (c==8) or (c==9) or (c==11) or (c==12):
            palabra = df2[c]
            #print("palabra:", palabra)
            count=0
            for char in df2[c]:
                #print("char", char)
                if count>2:
                    df2[c]=df2[c].replace(df2[c][count], "*")
                    #char="*"
                count=count+1

    print ("final:", df2)

    # except:
    #     print("Usuario no encontrado")

    return

permisoIntermedio('BF000002999')

