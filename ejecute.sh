#!/bin/bash

python -m venv my_env
source my_env/bin/activate
pip install -r requirements.txt
python scrapper.py