from Lectura.LecturaExcel import Leer_excel
from Preprocesado.ModifcacionBaseDeDatos import Limitar_tiempos, Arreglar_vacios
from Utilidad.ConversionFechas import Date_To_Data 
from Entrenamiento.MetodosDeEntrenamiento import Entrenamiento_cat
from Graficos.GeneracionDeGraficas import Graficacion_loss
import pandas as pd

if __name__ == "__main__":
    df = Leer_excel(r'C:\Users\lemus\Documents\TESISAZTECA\Codigo\Datos\Datosrecorte_limpieza_de_motivosextra.xlsx')
    df = Date_To_Data(df,"Fecha/Hora de apertura")
    LimiteSuperior=40
    LimiteInferior=1
    df=Limitar_tiempos(df,LimiteSuperior,LimiteInferior)
    df=Arreglar_vacios(df,14000)
    ColumnasIgnoradas = ['Fecha/Hora de apertura','tiempo_solucion_horas','Fecha_Solucion']
    X=df.drop(columns=ColumnasIgnoradas)
    y=df['tiempo_solucion_horas']
    Ls="MAE"
    modelo=Entrenamiento_cat(X,y,ite=500,Depth=8,Ls=Ls)  
    Graficacion_loss(modelo,Ls)