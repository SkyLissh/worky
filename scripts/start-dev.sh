#!/usr/bin/env bash

set -o errexit
set -o nounset

python manage.py makemigrations
python manage.py migrate

python -Wd manage.py runserver 0.0.0.0:8000
