Запускаем сборку докер-компоуз.
docker-compose -p notekeeper up -d

Подготавливаем все к работе.
. begin_work.sh 

Заполняем БД (если нужно).
. restore.sh 