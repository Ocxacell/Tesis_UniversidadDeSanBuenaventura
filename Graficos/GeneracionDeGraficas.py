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