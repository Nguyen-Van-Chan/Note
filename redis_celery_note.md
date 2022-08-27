Chú ý khi dùng celery với docker và redis 

Cách check connection với redis trong docker. 

```
# ví dụ với redis đc cáu hình trong docker file 
docker-compose run redis redis-cli -u redis://redis:6379/0
# Tổng quát 
docker-compose run redis redis-cli -u redis://host:6379/0
# có thể thử 
docker-compose run redis redis-cli -u redis://0.0.0.0:6379/0
docker-compose run redis redis-cli -u redis://127.0.0.1:6379/0
```

```python 
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_BACKEND_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
```

Cấu hình cache 
```python 
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/0',
        'KEY_PREFIX': 'rootapp',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

```
YML config docker compose file 

```p
version: '3.6'

services:
  db:
    image: postgres:10
    ports:
      - "5432:5432"
    environment:
      POSTGRES_PASSWORD: rootapp123
    volumes:
      - postgres_data:/var/lib/postgresql/data/
  redis:
    image: "redis:alpine"
    volumes:
      - redis_data:/data
    ports:
      - "6379:6379"
  worker:
    build: .
    command: celery worker --app rootapp --loglevel info --logfile celery-worker.log
    volumes:
      - .:/code
    depends_on:
      - redis
  schedule:
    build: .
    command: celery beat --app rootapp --loglevel info --logfile celery-beat.log
    volumes:
      - .:/code
    depends_on:
      - redis
  web:
    build: .
    command: bash -c "python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8000"
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
      - redis
  document:
    image: swaggerapi/swagger-ui
    volumes:
      - .:/app
    ports:
      - "1234:8080"
    environment:
      SWAGGER_JSON: /app/docs/openapi.json
volumes:
  postgres_data:
  redis_data:

```
