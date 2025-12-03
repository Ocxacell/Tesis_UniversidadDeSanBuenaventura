import pandas as pd

def Limitar_tiempos(RangoSuperior, RangoInferior):
    df = df[df["tiempo_solucion_horas"] >= RangoInferior]
    df = df.drop(df[df["tiempo_solucion_horas"] > RangoSuperior].index)