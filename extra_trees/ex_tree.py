import sys

from sklearn import datasets
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.model_selection import train_test_split

def main():
    iris = datasets.load_iris()
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)

    ex_model = ExtraTreesClassifier()
    ex_model.fit(x_train, y_train)

    ex_score = ex_model.score(x_test, y_test)
    print(f"ex tree score: {ex_score}")

    rf_model = RandomForestClassifier()
    rf_model.fit(x_train, y_train)

    rf_score = rf_model.score(x_test, y_test)
    print(f"rf score: {rf_score}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
