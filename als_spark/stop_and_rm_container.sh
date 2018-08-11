#!/bin/bash

echo "stop&remove docker container"
CONTAINER_ID=`docker container ls -a | awk '!/(CONTAINER ID)/ {print $1}'`
docker stop ${CONTAINER_ID}
docker rm ${CONTAINER_ID}

echo "remove datasets"
CURRENT_PATH=`pwd`
rm -rf ${CURRENT_PATH}/work/ml-latest-small

echo 'DONE'
