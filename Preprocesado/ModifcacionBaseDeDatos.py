import pandas as pd

def Limitar_tiempos(df,RangoSuperior, RangoInferior,target):
    df = df[df[target] >= RangoInferior]
    df = df.drop(df[df[target] > RangoSuperior].index)
    return df

def Arreglar_vacios(df, NanAdmitidos=1000):
    print("Limpieza de features")
    col_names = df.columns.tolist()
    for col in col_names:
        print("Distrubucion de la columna:", col)
        print("Columnas nulas")
        vacias=df[col].isnull().sum()
        print(vacias)
        if vacias < NanAdmitidos:
            df = df.dropna(subset=[col])
        else:
            df[col] = df[col].fillna('Desconocido')
    return df

def Eliminar_filas_por_valor(df, columna, valor):
    df = df[df[columna] != valor]
    return df


def Umbral_Para_Outliners(df,rangosuperior,rangoinferior,Porcentaje,Seed,target):
    mask = (df[target] >= rangoinferior) & (df[target] <= rangosuperior)
    df_aislado = df[mask]
    df_otros = df[~mask]

    df_sub = df_aislado.sample(frac=Porcentaje, random_state=Seed)

    df_balanceado = pd.concat([df_sub, df_otros])

    print("Original:", len(df))
    print("Balanceado:", len(df_balanceado))

    suma = ((df[target] >= rangoinferior) & (df[target] <= rangosuperior)).sum()
    print("Casos entre",rangoinferior," y ",rangosuperior," antes del submuestreo:", suma)
    df = df_balanceado
    casos_filtrado = ((df[target] >= rangoinferior) & (df[target] <= rangosuperior)).sum()
    print("Casos entre",rangoinferior," y ",rangosuperior," después del submuestreo:", casos_filtrado)
    return df
