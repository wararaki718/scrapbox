#!/bin/bash

# create network
docker network create flask_net

# build image
docker-compose build --no-cache
