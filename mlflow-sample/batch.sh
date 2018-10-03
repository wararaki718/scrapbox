#!/bin/bash

RUN_ID=
MODEL_PATH=
mlflow pyfunc predict -m $MODEL_PATH -r $RUN_ID -i boston_data.csv -o boston_pred.csv