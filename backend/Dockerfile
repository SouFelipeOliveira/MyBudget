#sintax=docker/dockerfile:1
FROM python:3.12
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV PATH="/scripts:${PATH}"

WORKDIR /app

RUN apt-get update && apt-get install -y libldap2-dev libsasl2-dev libssl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt


COPY . /app/
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static


CMD ["entrypoint.sh"]

