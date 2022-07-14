import pandas as pd

datos = pd.read_csv("baseClientesHackaton2022.csv")
df = pd.DataFrame(datos)

def permisoIntermedio(idCliente):
    df = pd.read_csv("./baseClientesHackaton2022.csv",index_col="idCliente",parse_dates=True)
    #idCliente = 'BF000002999'
    try:
        df2 =df.loc[idCliente].tolist()
        for c in range(12):
            if(c==1) or (c==2) or (c==3) or (c==6) or (c==7) or (c==8) or (c==9) or (c==11) or (c==12):
                palabra = df2[c]

                df2[c]=palabra[slice(3)]+"****"

        print ("final:", df2)

    except:
        print("Usuario no encontrado")

    return

#permisoIntermedio('BF000002999')


