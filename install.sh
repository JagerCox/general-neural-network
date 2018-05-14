#!/bin/bash
rm -rf virtualenv
virtualenv -p python3 virtualenv
source virtualenv/bin/activate
pip install -r requeriments.txt
