
import pandas as pd
import numpy as np
import pickle

#from pyml.model.dataframe_model import DataFrameModel
from sklearn.externals import joblib

#class LogisticRegressionModel(DataFrameModel)
class LogisticRegressionModel:
    def __init__(self):
#         super(LogisticRegressionModel, self).__init__()
        # load the model weights and feature name
        self.clf = joblib.load('weights.pkl')
        self.feature_columns = pickle.load(open('feature_columns.pkl', 'rb'))

    def predict(self, df):
        df['probability'] = self.clf.predict_proba(
            df[self.feature_columns]
        )[:, 0]
        return df