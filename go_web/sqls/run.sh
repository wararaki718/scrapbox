#!/bin/bash

# up postgres
docker run --name sample-psql -p 5432:5432 -d postgres

# create table & insert sample data
psql -h 127.0.0.1 -p 5432 -U postgres -f sample.sql

# check table info
psql -h 127.0.0.1 -p 5432 -U postgres -f select.sql

# stop postgres docker
# docker stop sample-psql