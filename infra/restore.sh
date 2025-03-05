#!/bin/bash

# chmod +x имя_скрипта.sh
# ./begin_work.sh

# Переменные
CONTAINER_NAME=notekeeper-web-1  # Имя контейнера PostgreSQL
#CONTAINER_NAME=notekeeper  # Имя контейнера PostgreSQL

# грузим дамп БД в контейнер
docker cp db.json $CONTAINER_NAME:/app/
docker exec -d $CONTAINER_NAME python3 manage.py loaddata db.json