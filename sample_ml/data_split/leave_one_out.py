'''
refs:
https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html#sklearn.model_selection.LeaveOneOut
'''

import sys

from sklearn import datasets
from sklearn.model_selection import LeaveOneOut


def main():
    iris = datasets.load_iris()
    data = iris.data
    target = iris.target

    # k-fold cross-validation
    loo = LeaveOneOut()
    for train_index, test_index in loo.split(data):
        x_train, x_test = data[train_index], data[test_index]
        y_train, y_test = target[train_index], target[test_index]

        print('data')
        print(x_train[:5])
        print(x_test)

        print('target')
        print(y_train[:5])
        print(y_test)

    return 0


if __name__ == '__main__':
    sys.exit(main())
