from Lectura.LecturaExcel import Leer_excel
from Preprocesado.ModifcacionBaseDeDatos import Limitar_tiempos, Arreglar_vacios, Eliminar_filas_por_valor
from Utilidad.ConversionFechas import Date_To_Data 
from Entrenamiento.MetodosDeEntrenamiento import Entrenamiento_cat
from Graficos.GeneracionDeGraficas import Graficacion_loss
import pandas as pd

if __name__ == "__main__":
    df = Leer_excel(r'C:\Users\lemus\Documents\TESISAZTECA\Codigo\Datos\BaseDeDatos.xlsx')
    df["Tiempo Total Ejecutado"] = pd.to_numeric(df["Tiempo Total Ejecutado"], errors='coerce')
    df = Date_To_Data(df,"Fecha/Hora de apertura")
    df = Eliminar_filas_por_valor(df,"Dificil acceso","NN")
    LimiteSuperior=3000
    LimiteInferior=1

    print(df)
    print("Yiempo")
    print(df["Tiempo Total Ejecutado"])
    df=Limitar_tiempos(df,LimiteSuperior,LimiteInferior,"Tiempo Total Ejecutado")
    df=Arreglar_vacios(df,14000)
    print(df)
    print("Yiempo")
    print(df["Tiempo Total Ejecutado"])
    ColumnasIgnoradas = ['Fecha/Hora de apertura','Número del caso',"Caso Asociador","Caso Nodo","Tiempo Total Ejecutado"]
    X=df.drop(columns=ColumnasIgnoradas)
    y=df["Tiempo Total Ejecutado"]
    Ls="MAE"
    modelo=Entrenamiento_cat(X,y,ite=10000,Depth=5,Ls=Ls,Lr=0.09)  
    Graficacion_loss(modelo,Ls)