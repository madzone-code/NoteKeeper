#!/bin/bash

# chmod +x имя_скрипта.sh
# ./begin_work.sh

# Переменные
CONTAINER_NAME=notekeeper-web-1  # Имя контейнера PostgreSQL
#CONTAINER_NAME=notekeeper  # Имя контейнера PostgreSQL

# грузим дамп БД
docker exec -it $CONTAINER_NAME python3 manage.py dumpdata > db.json