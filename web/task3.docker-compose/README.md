![django_logo](django_logo.png)

#### Для запуска образа для разработки выполните:

```
docker-compose up -d --build
```

#### В случае образа для релиза выполните:

```
docker-compose -f docker-compose.prod.yml up -d --build
```

#### В отличие от обычного образа, в случае продакшена нужно дополнительно выполнять миграции и сбор статических файлов:

```
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear 
```

