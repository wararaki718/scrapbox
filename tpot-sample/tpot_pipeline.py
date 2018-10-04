import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.kernel_approximation import RBFSampler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=42)

# Average CV score on the training set was:0.9822134387351777
exported_pipeline = make_pipeline(
    RBFSampler(gamma=0.30000000000000004),
    GradientBoostingClassifier(learning_rate=0.01, max_depth=10, max_features=0.7000000000000001, min_samples_leaf=11, min_samples_split=11, n_estimators=100, subsample=0.3)
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
