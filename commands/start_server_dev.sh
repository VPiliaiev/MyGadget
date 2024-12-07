#!/bin/sh
chmod +x ./commands/start_server_dev.sh

python src/manage.py migrate
python src/manage.py check

python src/manage.py runserver 0:8000