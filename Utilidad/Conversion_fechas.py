import pandas as pd

def DateToData(df,DateCol):
    df[DateCol] = pd.to_datetime(df[DateCol], errors="coerce")

    #Extraer características temporales
    df["Mes_apertura"] = df[DateCol].dt.month
    df["Día_apertura"] = df[DateCol].dt.day
    df["Hora_apertura"] = df[DateCol].dt.hour
    df["Día_semana_apertura"] = df[DateCol].dt.weekday
    return df