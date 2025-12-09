import pandas as pd

def Leer_excel(archivo_excel: str):
    ###############Lectura del excel###############
    df = pd.read_excel(archivo_excel)
    print("Datos cargados correctamente")
    return df