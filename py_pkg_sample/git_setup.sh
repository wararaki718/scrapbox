#!/bin/bash

pip install 'git+https://github.com/wararaki/scrapbox.git#egg=hello&subdirectory=py_pkg_sample/pkg'
echo ""
python test.py
echo ""
pip uninstall -y hello