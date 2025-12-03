from Lectura.Lectura_excel import leer_excel 
from Utilidad.Conversion_fechas import DateToData
import pandas as pd
if __name__ == "__main__":
    df = leer_excel(r'C:\Users\lemus\Documents\TESISAZTECA\Datos\Datosrecorte_limpieza_de_motivosextra.xlsx')
    DateToData(df,"Fecha/Hora de apertura")
    print(df["Mes_apertura"])
    df[DateCol].isna().sum()
