#!/bin/bash

echo "Migrate database..."
python manage.py migrate

echo "Starting a server"
python manage.py runserver 0.0.0.0:8000

exec "$@"