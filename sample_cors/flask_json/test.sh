#!/bin/bash

curl -XPOST localhost:5556/msg -H 'Content-Type: application/json' -d '{"msg": "hello"}'