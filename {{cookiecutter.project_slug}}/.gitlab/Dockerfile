FROM orbisk/django-test:3.11 as base

# where your code lives
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install lsb-release -y
RUN apt-get -y install apt-utils


RUN pip install --upgrade pip

# install dependencies
COPY requirements/base.txt requirements/base.txt
COPY requirements/production.txt requirements/production.txt
RUN pip install -r requirements/production.txt

COPY . .
