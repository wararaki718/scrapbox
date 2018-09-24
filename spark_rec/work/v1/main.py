'''
recommendation batch
'''
from argparse import ArgumentParser
import logging
import os
import sys

import pandas as pd
from pyspark.ml.recommendation import ALS
from pyspark.sql import SparkSession

import yaml


# get logger
logger = logging.getLogger(__name__)


def parse_command_options():
    parser = ArgumentParser()
    parser.add_argument("--config-file", dest="config_file", default="./config.yml")
    return parser.parse_args()


def init_logger():
    logging.root.setLevel(level='INFO')
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')


def load_config(config_file):
    with open(config_file) as f:
        config = yaml.load(f)
    return config


def get_spark_session():
    spark = SparkSession.builder.getOrCreate()
    return spark


def load_data(spark, data_path):
    data_format = os.path.splitext(data_path)[-1][1:]
    df = spark.read.format(data_format).load(data_path, inferSchema=True, header=True)
    return df


def main():
    '''
    main function
    '''
    logger.info("start recommend")
    options = parse_command_options()
    init_logger()
    config = load_config(options.config_file)
    spark = get_spark_session()
    
    # load data
    logger.info("start : load data")
    df = load_data(spark, config.get("data").get("path"))
    logger.info("finish: load data")

    # load model
    logger.info("start : fit model")
    als = ALS(**config.get('recommend').get('als'))
    model = als.fit(df)
    logger.info("finish: fit model")

    # show results
    logger.info("all users")
    logger.info(model.recommendForAllUsers(5).toPandas())

    logger.info("all items")
    logger.info(model.recommendForAllItems(5).toPandas())
    logger.info("done")

    return 0


if __name__ == "__main__":
    sys.exit(main())
