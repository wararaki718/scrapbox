#!/bin/bash

pip install ./pkg
echo ""
python test.py
echo ""
pip uninstall -y hello