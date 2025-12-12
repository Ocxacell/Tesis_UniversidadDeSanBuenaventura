import pandas as pd
from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split

def Entrenamiento_cat (X,y,ite=1000,Lr=0.05,Ls="MAE",Depth=5,Verbose=200,Seed=15,EarlyStop=200):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=15)
    # ⿨ Identificar features categóricas y numéricas
    cat_features = X_train.select_dtypes(include=["object"]).columns.tolist()
    model = CatBoostRegressor(
        task_type="CPU",
        iterations=ite,
        learning_rate=Lr,
        depth=Depth,
        loss_function=Ls,
        cat_features=cat_features,
        eval_metric=Ls,
        verbose=Verbose,
        random_seed=Seed,
        early_stopping_rounds=EarlyStop
    )
    model.fit(
        X_train, y_train,
        cat_features=cat_features,
        eval_set=(X_test, y_test),
        use_best_model=True,
        plot=False
    )
    Y_pred= model.predict(X_test)
    return model,Y_pred,y_test
    