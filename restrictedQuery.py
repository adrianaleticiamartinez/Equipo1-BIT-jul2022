import pandas as pd
import numpy as np
def searchClient(idCliente):
    df = pd.read_csv("./baseClientesHackaton2022.csv",index_col="idCliente",parse_dates=True)
    #idCliente = 'BF000002999'
    try:
        df2 =df.loc[idCliente]
        print(df2[['nombre','sexo','segmento','cuenta']].head(5))
    except:
        print("Usuario no encontrado")
