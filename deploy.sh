#!/bin/bash
git pull
./venv/bin/pip install -r ./requirements.txt
./venv/bin/python3 ./manage.py migrate
./venv/bin/python3 ./manage.py runserver 45.132.18.176:80 &