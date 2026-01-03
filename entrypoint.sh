#!/usr/bin/env sh
set -e

python manage.py migrate --noinput
python manage.py collectstatic --noinput
chmod -R a+rX /app/staticfiles || true

# If you have gunicorn in requirements, use it:
if command -v gunicorn >/dev/null 2>&1; then
  exec gunicorn app404.wsgi:application --bind 0.0.0.0:8000 --workers 2 --timeout 60
else
  exec python manage.py runserver 0.0.0.0:8000
fi
