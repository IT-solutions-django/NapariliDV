#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

celery -A NapariliDV worker -l info -P prefork &
celery -A NapariliDV beat -l info &
celery -A NapariliDV flower -l info &
gunicorn NapariliDV.wsgi:application --bind 0.0.0.0:8000 &

wait