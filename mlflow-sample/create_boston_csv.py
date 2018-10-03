'''
generate boston dataset csv.
'''
from argparse import ArgumentParser
import logging
import sys

import pandas as pd
from sklearn import datasets

logger = logging.getLogger(__name__)


def init_logger():
    logging.root.setLevel(level="INFO")
    logging.basicConfig(format='%(asctime)s- %(name)s - %(levelname)s - %(message)s')


def parse_command_options():
    parser = ArgumentParser()
    parser.add_argument("--data-path", dest='data_path', default='boston_data.csv')
    parser.add_argument("--target-path", dest='target_path', default='boston_target.csv')
    return parser.parse_args()


def create_csv(data, file_path, header=None):
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=None, header=header)


def main():
    options = parse_command_options()
    init_logger()

    boston = datasets.load_boston()

    create_csv(boston.data, options.data_path, header=boston.feature_names)
    logger.info(f"{options.data_path} is created.")

    create_csv(boston.target, options.target_path)
    logger.info(f"{options.target_path} is created.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
