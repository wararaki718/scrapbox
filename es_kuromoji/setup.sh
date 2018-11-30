#!/bin/bash
echo "set index"
curl -H "Content-Type: application/json" -XPUT localhost:9200/kamen -d '@jsons/index.json'
python bulk.py

echo "check"
curl -XGET localhost:9200/_cat/plugins
curl -XGET localhost:9200/kamen"?pretty"
echo "setup done"