#!/bin/bash

echo "search01"
curl -H 'Content-Type: application/json' -XGET localhost:9200/kamen/rider/_search"?pretty" -d @jsons/search01.json

echo "search02"
curl -H 'Content-Type: application/json' -XGET localhost:9200/kamen/rider/_search"?pretty" -d @jsons/search02.json

echo "search03"
curl -H 'Content-Type: application/json' -XGET localhost:9200/kamen/rider/_search"?pretty" -d @jsons/search03.json

echo "search04"
curl -H 'Content-Type: application/json' -XGET localhost:9200/kamen/rider/_search"?pretty" -d @jsons/search04.json