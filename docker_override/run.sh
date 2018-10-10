#!/bin/bash
echo "original"
docker-compose -f docker-compose.yml up

echo "override"
docker-compose -f docker-compose.yml -f docker-compose.override.yml up

echo "DONE"
