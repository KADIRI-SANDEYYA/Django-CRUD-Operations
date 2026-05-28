#!/bin/bash
python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn Django_CRUD_Operations.wsgi:application --bind 0.0.0.0:$PORT