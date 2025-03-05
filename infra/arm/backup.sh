#!/bin/bash

# chmod +x имя_скрипта.sh
# ./begin_work.sh

# Переменные
CONTAINER_NAME=notekeeper  # Имя контейнера

# грузим дамп БД
docker exec -it $CONTAINER_NAME python3 manage.py dumpdata > db.json
docker cp $CONTAINER_NAME:/app/ db.json