#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

echo "Flushing database"
python manage.py flush --noinput

echo "Importing test data"
python manage.py loaddata fixtures/shop_db.json

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000