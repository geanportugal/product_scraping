#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar
set -e
DOCKER_CONTAINER_NAME="mongodb"
function is_mongodb_ready() {
    docker exec "$DOCKER_CONTAINER_NAME" mongo --eval "db.adminCommand('ping')" &> /dev/null
    return $?
}


while is_mongodb_ready; do
  echo "🟡 Waiting for Mongo Database Startup) ..."
  sleep 2
done

python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8000

