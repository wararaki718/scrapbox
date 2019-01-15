#!/bin/bash
cd json
curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/kamen/rider/_bulk"?pretty" --data-binary "@data.json"
cd ..
echo "bulk done"