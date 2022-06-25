#!/usr/bin/env bash

set -o errexit
set -o nounset

python manage.py migrate

rm -rf ./app/static/css/dist
tailwind -i ./app/static/css/input.css -o ./app/static/css/dist/styles.css --minify
python manage.py collectstatic --no-input

gunicorn app.wsgi:application --bind 0.0.0.0:8000 --workers 
