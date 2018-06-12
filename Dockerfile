FROM python:3.6-alpine3.7

COPY requirements.txt /tmp/

RUN apk update --no-cache \
  && apk add --no-cache git \
  && apk add --no-cache --virtual .postgres-deps py3-psycopg2 postgresql-libs postgresql-dev \
  && apk add --no-cache --virtual .build-deps libffi-dev build-base zlib-dev jpeg-dev \
  && apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/main libressl2.7-libcrypto \
  && apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing geos gdal \
  && pip install -r /tmp/requirements.txt --no-cache-dir \
  && wget https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.6.1.tar.gz && rm dockerize-linux-amd64-v0.6.1.tar.gz \
  && apk del .build-deps && apk del .postgres-deps

CMD ["python3"]
