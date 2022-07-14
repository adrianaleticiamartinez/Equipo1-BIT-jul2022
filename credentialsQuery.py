import pandas as pd
import numpy as np
def searchUser(idUsuario, password):
    df = pd.read_csv("./baseUsuarios.csv",index_col="usuario",parse_dates=True)
    #idCliente = 'BF000002999'
    try:
        #print(df.head(5))
        df2 =df.loc[idUsuario].tolist()
        if (password == df2[0]):
            return df2[5]
        else:
            return "Credenciales invalidas"
        #print(df2[['nombre','sexo','segmento','cuenta']].head(5))
    except:
       return "Credenciales invalidas" 