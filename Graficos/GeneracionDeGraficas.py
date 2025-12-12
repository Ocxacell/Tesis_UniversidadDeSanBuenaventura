import matplotlib.pyplot as plt
from catboost import CatBoostRegressor


def Graficacion_loss(model,Ls):
    metricas = model.get_evals_result()

    train_loss = metricas['learn'][Ls]
    val_loss = metricas['validation'][Ls]
    plt.plot(train_loss,label="Funcion de perdidas del entrenamiento")
    plt.plot(val_loss,label="Funcion de perdidas de la validacion")
    plt.xlabel("Iteracion")
    plt.ylabel(Ls)
    plt.legend()
    plt.grid()
    plt.show()


def Graficar_frecuencia(df, columna_target, modo="curva"):
    """
    Grafica la frecuencia del target como curva o histograma.
    
    Parámetros:
    df : DataFrame
    columna_target : str -> nombre de la columna target
    modo : "curva" o "hist" 
    """
    # Eliminar valores nulos por seguridad
    serie = df[columna_target].dropna()

    # Calcular la frecuencia de valores
    cont = serie.value_counts().sort_index()

    plt.figure(figsize=(8, 5))

    if modo == "curva":
        plt.plot(cont.index, cont.values, marker="o")
        plt.title(f"Frecuencia del target: {columna_target} (Curva)")
        plt.xlabel("Valor del target")
        plt.ylabel("Frecuencia")

    elif modo == "hist":
        plt.hist(serie, bins=20)
        plt.title(f"Distribución del target: {columna_target} (Histograma)")
        plt.xlabel("Valor del target")
        plt.ylabel("Frecuencia")

    else:
        print("Modo inválido: usa 'curva' o 'hist'")
        return

    plt.grid(True)
    plt.show()

def Grafica_prediccion(df):
    plt.figure(figsize=(7, 6))
    plt.scatter(df["Real"], df["Predicho"], alpha=0.6)
    max_val = max(df["Real"].max(), df["Predicho"].max())
    min_val = min(df["Real"].min(), df["Predicho"].min())
    plt.plot([min_val, max_val], [min_val, max_val], linestyle="--")

    plt.xlabel("Real")
    plt.ylabel("Predicho")
    plt.title("Comparación: Real vs Predicho")
    plt.grid(True)
    plt.show()