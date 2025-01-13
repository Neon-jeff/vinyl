web: python manage.py collectstatic --noinput && python manage.py makemigrations && python manage.py migrate && gunicorn core.wsgi --timeout 120 --workers=3 --threads=3 --worker-connections=1000
