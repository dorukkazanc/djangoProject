#!/bin/sh

echo "Postgres bekleniyor"
while ! nc -z db 5432; do
  sleep 1
done

echo "migration yapılıyor"
python manage.py migrate

echo "initial datalar yükleniyor"
python manage.py loaddata ./dump.json

python manage.py runserver 0.0.0.0:8000