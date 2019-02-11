'''
refs:
https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold
'''

import sys

from sklearn import datasets
from sklearn.model_selection import KFold


def main():
    iris = datasets.load_iris()
    data = iris.data
    target = iris.target

    # k-fold cross-validation
    kf = KFold(n_splits=2, shuffle=True)
    for train_index, test_index in kf.split(data):
        x_train, x_test = data[train_index], data[test_index]
        y_train, y_test = target[train_index], target[test_index]

        print('data')
        print(x_train[:5])
        print(x_test[:5])

        print('target')
        print(y_train[:5])
        print(y_test[:5])

    return 0


if __name__ == '__main__':
    sys.exit(main())
