#!/bin/sh
python manage.py migrate

if [ -z "$PORT" ]; then
  export PORT=8000
fi
/usr/local/bin/gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 larixon_tst.wsgi
