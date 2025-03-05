#!/bin/bash

# chmod +x имя_скрипта.sh
# ./begin_work.sh

# Переменные
CONTAINER_NAME=notekeeper-web-1  # Имя контейнера PostgreSQL

# работаем с миграциями
docker exec -it $CONTAINER_NAME python3 manage.py makemigrations
docker exec -it $CONTAINER_NAME python3 manage.py migrate
# суперюзер
docker exec -it $CONTAINER_NAME python3 manage.py createsuperuser
# собираем статику
docker exec -it $CONTAINER_NAME python3 manage.py collectstatic
# грузим дамп БД
docker exec -it $CONTAINER_NAME python3 manage.py loaddata db.json