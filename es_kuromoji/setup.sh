#!/bin/bash
docker run -t kamen -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node"
curl -s -XPUT localhost:9200/kamen -d @index.json
curl -XPOST -s -H "Content-Type: application/x-ndjson" localhost:9200/_bulk -d @data.ndjson