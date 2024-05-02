# Cookiecutter Django

[![Build Status](https://img.shields.io/github/actions/workflow/status/cookiecutter/cookiecutter-django/ci.yml?branch=master)](https://github.com/cookiecutter/cookiecutter-django/actions/workflows/ci.yml?query=branch%3Amaster)
[![Documentation Status](https://readthedocs.org/projects/cookiecutter-django/badge/?version=latest)](https://cookiecutter-django.readthedocs.io/en/latest/?badge=latest)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/cookiecutter/cookiecutter-django/master.svg)](https://results.pre-commit.ci/latest/github/cookiecutter/cookiecutter-django/master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

[![Updates](https://pyup.io/repos/github/cookiecutter/cookiecutter-django/shield.svg)](https://pyup.io/repos/github/cookiecutter/cookiecutter-django/)
[![Join our Discord](https://img.shields.io/badge/Discord-cookiecutter-5865F2?style=flat&logo=discord&logoColor=white)](https://discord.gg/uFXweDQc5a)
[![Code Helpers Badge](https://www.codetriage.com/cookiecutter/cookiecutter-django/badges/users.svg)](https://www.codetriage.com/cookiecutter/cookiecutter-django)

Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter), Cookiecutter Django is a framework for jumpstarting
production-ready Django projects quickly.

- Documentation: <https://cookiecutter-django.readthedocs.io/en/latest/>
- See [Troubleshooting](https://cookiecutter-django.readthedocs.io/en/latest/troubleshooting.html) for common errors and obstacles
- If you have problems with Cookiecutter Django, please open [issues](https://github.com/cookiecutter/cookiecutter-django/issues/new) don't send
  emails to the maintainers.

## Features

- For Django 4.2
- Works with Python 3.11
- Renders Django projects with 100% starting test coverage
- Twitter [Bootstrap](https://github.com/twbs/bootstrap) v5
- [12-Factor](https://12factor.net) based settings via [django-environ](https://github.com/joke2k/django-environ)
- Secure by default. We believe in SSL.
- Optimized development and production settings
- Comes with custom user model ready to go
- Optional basic ASGI setup for Websockets
- Optional custom static build using Gulp or Webpack
- Send emails via [Anymail](https://github.com/anymail/django-anymail) (using [Mailgun](http://www.mailgun.com/) by default or Amazon SES if AWS is selected cloud provider, but switchable)
- Media storage using Amazon S3, Google Cloud Storage, Azure Storage or nginx
- Docker support using [docker-compose](https://github.com/docker/compose) for development and production (using [Traefik](https://traefik.io/) with [LetsEncrypt](https://letsencrypt.org/) support)
- [Procfile](https://devcenter.heroku.com/articles/procfile) for deploying to Heroku
- Instructions for deploying to [PythonAnywhere](https://www.pythonanywhere.com/)
- Run tests with unittest or pytest
- Customizable PostgreSQL version
- Default integration with [pre-commit](https://github.com/pre-commit/pre-commit) for identifying simple issues before submission to code review

## Optional Integrations

_These features can be enabled during initial project setup._

- Serve static files from Amazon S3, Google Cloud Storage, Azure Storage or [Whitenoise](https://whitenoise.readthedocs.io/)
- Configuration for [Celery](https://docs.celeryq.dev) and [Flower](https://github.com/mher/flower) (the latter in Docker setup only)
- Integration with [Mailpit](https://github.com/axllent/mailpit/) for local email testing
- Integration with [Sentry](https://sentry.io/welcome/) for error logging

## Constraints

- Only maintained 3rd party libraries are used.
- Uses PostgreSQL everywhere: 13 - 15 ([MySQL fork](https://github.com/mabdullahadeel/cookiecutter-django-mysql) also available).
- Environment variables for configuration (This won't work with Apache/mod_wsgi).


## Usage

First, get Cookiecutter. Trust me, it's awesome:

    $ pip install "cookiecutter>=1.7.0"

Now run it against this repo:

    $ cookiecutter https://github.com/singularit-de/cookiecutter-django

You'll be prompted for some values. Provide them, then a Django project will be created for you.


Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?

For local development, see the following:

- [Developing locally](http://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html)
- [Developing locally using docker](http://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html)
