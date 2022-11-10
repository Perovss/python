FROM docker.io/library/python:3.8
RUN wget https://github.com/Perovss/stocks_products/archive/refs/heads/main.zip && unzip -a main.zip && rm main.zip
WORKDIR /stocks_products-main
COPY files/settings.py stocks_products
RUN pip install --upgrade pip && pip install -r requirements.txt \
    && python3 manage.py makemigrations && python3 manage.py migrate \
    && python3 manage.py collectstatic --noinput
EXPOSE 8000
CMD gunicorn stocks_products.wsgi -b 0.0.0.0:8000
