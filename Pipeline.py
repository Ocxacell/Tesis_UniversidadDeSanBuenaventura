from Lectura.Lectura_excel import leer_excel
from Preprocesado.ModificacionBaseDeDatos import Limitar_tiempos
from Utilidad.Conversion_fechas import DateToData
import pandas as pd
if __name__ == "__main__":
    df = leer_excel(r'C:\Users\lemus\Documents\TESISAZTECA\Codigo\Datos\Datosrecorte_limpieza_de_motivosextra.xlsx')
    df = DateToData(df,"Fecha/Hora de apertura")
    
