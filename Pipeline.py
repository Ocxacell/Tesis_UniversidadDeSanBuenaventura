from Lectura.Lectura_excel import leer_excel
from Preprocesado.ModifcacionBaseDeDatos import Limitar_tiempos, Arreglar_vacios
from Utilidad.Conversion_fechas import Date_To_Data 
import pandas as pd
if __name__ == "__main__":
    df = leer_excel(r'C:\Users\lemus\Documents\TESISAZTECA\Codigo\Datos\Datosrecorte_limpieza_de_motivosextra.xlsx')
    df = Date_To_Data(df,"Fecha/Hora de apertura")
    LimiteSuperior=40
    LimiteInferior=1
    Limitar_tiempos(df,LimiteSuperior,LimiteInferior)
    Arreglar_vacios(df,14000)
    ColumnasIgnoradas = ['Fecha/Hora de apertura','tiempo_solucion_horas','Fecha_Solucion','tiempo_solucion_log']
    X=df.drop(columns=ColumnasIgnoradas)
    