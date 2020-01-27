# pidgeotto-web

# Comandos para instalar Celery
*pip install -U "celery[redis]"
*sudo apt install redis-server

# Comando para ver registros
*celery worker -A pidgeotto.celery --loglevel=info

# Comando para actualizar celery(debe de mantenerse activo)
*celery -A pidgeotto.celery beat
