#!/bin/bash
curl -XPOST http://0.0.0.0:5555/predict -H 'Content-Type: application/json' -d '{"x": [1, 0, 0, 1]}'