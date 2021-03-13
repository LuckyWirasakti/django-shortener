python3 manage.py collectstatic --no-input
python3 manage.py migrate --no-input
gunicorn core.wsgi --bind 0.0.0.0:8000