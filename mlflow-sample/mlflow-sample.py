import os
import sys

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet

import mlflow
import mlflow.sklearn


def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


def main():
    # create dataset
    boston = datasets.load_boston()
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.33)

    alpha = 0.1
    l1_ratio = 0.6
    with mlflow.start_run():
        e_net = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
        e_net.fit(x_train, y_train)

        y_pred = e_net.predict(x_test)

        (rmse, mae, r2) = eval_metrics(y_test, y_pred)

        print(f'Elasticnet model (alpha={alpha}, l1_ratio={l1_ratio}):')
        print(f'  RMSE: {rmse}')
        print(f'  MAE : {mae}')
        print(f'  R2  : {r2}')

        mlflow.log_param('alpha', alpha)
        mlflow.log_param('l1_ratio', l1_ratio)
        mlflow.log_metric('rmse', rmse)
        mlflow.log_metric('r2', r2)
        mlflow.log_metric('mae', mae)

        mlflow.sklearn.log_model(e_net, 'model')

    return 0

if __name__ == "__main__":
    sys.exit(main())
