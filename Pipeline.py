from Lectura.Lectura_excel import leer_excel
from Preprocesado.ModifcacionBaseDeDatos import Limitar_tiempos, Arreglar_vacios
from Utilidad.Conversion_fechas import Date_To_Data 
from Entrenamiento.MetodosDeEntrenamiento import Entrenamiento_cat
import pandas as pd
if __name__ == "__main__":
    df = leer_excel(r'C:\Users\lemus\Documents\TESISAZTECA\Codigo\Datos\Datosrecorte_limpieza_de_motivosextra.xlsx')
    df = Date_To_Data(df,"Fecha/Hora de apertura")
    LimiteSuperior=40
    LimiteInferior=1
    df=Limitar_tiempos(df,LimiteSuperior,LimiteInferior)
    df=Arreglar_vacios(df,14000)
    ColumnasIgnoradas = ['Fecha/Hora de apertura','tiempo_solucion_horas','Fecha_Solucion']
    X=df.drop(columns=ColumnasIgnoradas)
    y=df['tiempo_solucion_horas']
    print(X)
    print(y)
    Entrenamiento_cat(X,y,ite=3000)