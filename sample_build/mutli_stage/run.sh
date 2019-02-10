#!/bin/bash
echo "START"
./app/appc
./app/appgo
python app/app.py
echo "DONE"
