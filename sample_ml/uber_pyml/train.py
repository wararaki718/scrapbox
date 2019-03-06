import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer

dataset = load_breast_cancer()
feature_columns = [name.replace(' ', '_') for name in dataset.feature_names.tolist()]
pandas_df = pd.DataFrame(data=np.c_[dataset.data, dataset.target], columns=feature_columns+['target'])

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    dataset.data,
    dataset.target,
    random_state=42
)

log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

# print(log_reg.predict_proba(pandas_df[feature_columns])[:10, 0])

# export the model weights
from sklearn.externals import joblib
joblib.dump(log_reg, 'prediction_model/weights.pkl')

# export feature columns
import pickle
pickle.dump(feature_columns, open('prediction_model/feature_columns.pkl', 'wb'))
