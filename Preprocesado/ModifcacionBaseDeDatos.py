import pandas as pd

def Limitar_tiempos(df,RangoSuperior, RangoInferior):
    df = df[df["tiempo_solucion_horas"] >= RangoInferior]
    df = df.drop(df[df["tiempo_solucion_horas"] > RangoSuperior].index)
    return df

def Arreglar_vacios(df, NanAdmitidos):
    col_names = df.columns.tolist()
    for col in col_names:
        print("Distruciion de la columna:", col)
        print("Columnas nulas")
        vacias=df[col].isnull().sum()
        print(vacias)
        if vacias < 1000:
            df = df.dropna(subset=[col])
        else:
            df[col] = df[col].fillna('Desconocido')
    return df