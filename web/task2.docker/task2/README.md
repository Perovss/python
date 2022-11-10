## Сборка образа

docker build --tag stocks_products .

## Запуск

docker run -d --publish 8000:8000 stocks_products

# Проверка работы  RestAPI  через PostMan

## Cоздание продукта

![](files/1.png)

## Обновление продукта

![2](files/2.png)

## Получение продуктов

![3](files/3.png)