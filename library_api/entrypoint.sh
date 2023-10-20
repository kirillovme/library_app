#!/bin/bash

python3 manage.py migrate
python3 manage.py collectstatic --noinput
exec gunicorn core.wsgi:application --bind 0.0.0.0:"$WEB_PORT"
