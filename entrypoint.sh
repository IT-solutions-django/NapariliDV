#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

echo "Происходит минификация CSS-файлов..."
for file in /var/www/static/css/*.css; do
    uglifycss "$file" > "${file%.css}.min.css"
    echo "Файл $file минифицирован"
done

echo "Происходит минификация JS-файлов..."
for file in /var/www/static/js/*.js; do
    uglifyjs "$file" -o "${file%.js}.min.js" --compress --mangle
    echo "Файл $file минифицирован"
done

celery -A NapariliDV worker -l info -P prefork &
celery -A NapariliDV beat -l info &
celery -A NapariliDV flower -l info &
gunicorn NapariliDV.wsgi:application --bind 0.0.0.0:8000 &

wait