FROM python:3.9-alpine3.13

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app

RUN  pip install --upgrade pip && \
    apk add --update --no-cache libxml2-dev &&\
    apk add --update --no-cache libxslt-dev && \
    apk add --update --no-cache zlib-dev && \
    apk add --update --no-cache libffi-dev && \
    apk add --update --no-cache openssl-dev && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev musl-dev && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt

EXPOSE 8080

#CMD ["python", "server.py"]