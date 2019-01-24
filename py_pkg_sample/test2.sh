#!/bin/bash

## test run

pip install ./pkg_with_item
python test2.py
pip uninstall hello -y
rm out.ipynb text.txt