import logging
import sys

from sklearn import datasets
from sklearn.model_selection import train_test_split
from tpot import TPOTClassifier


logger = logging.getLogger(__name__)

def init_logger():
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(name)s :%(message)s",
        level='INFO'
    )


def main():
    init_logger()

    # load data
    iris = datasets.load_iris()
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target)

    # pipeline fit
    pipeline_optimizer = TPOTClassifier(generations=5, population_size=20, cv=5, random_state=42, verbosity=2)
    pipeline_optimizer.fit(x_train, y_train)
    
    # test
    score = pipeline_optimizer.score(x_test, y_test)
    logger.info(f"score: {score}")

    # export
    pipeline_optimizer.export("tpot_pipeline.py")

    return 0


if __name__ == "__main__":
    sys.exit(main())
