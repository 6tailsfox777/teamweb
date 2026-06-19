#!/bin/sh

set -e

printf 'Waiting for MySQL at db:3306...'
while ! python -c 'import socket; s=socket.socket(); s.settimeout(1); s.connect(("db", 3306)); s.close()'; do
  printf '.'
  sleep 1
done
printf '\nMySQL is available, starting Django.\n'
exec python manage.py runserver 0.0.0.0:8000
