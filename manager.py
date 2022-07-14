import pandas as pd

def managerQuery(id):
    try:
        df = pd.read_csv(
            'baseClientesHackaton2022.csv', index_col="idCliente",
            parse_dates=True
        )


        print(df.loc[id])
    except:
        print("Cliente no encontrado")