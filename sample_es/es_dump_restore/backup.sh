#!/bin/bash
# setup data
curl -X PUT "localhost:9200/_snapshot/my_backup?pretty" -H 'Content-Type: application/json' -d'
{
  "type": "fs",
  "settings": {
    "location": "/var/lib/elasticsearch/snapshots"
  }
}
'

# show info
curl -X GET "localhost:9200/_snapshot/my_backup?pretty"

# output snapshot
curl -X PUT "localhost:9200/_snapshot/my_backup/snapshot_1?wait_for_completion=true&pretty"

# show info
curl -X GET "localhost:9200/_snapshot/my_backup/snapshot_1?pretty"

echo "backup done."