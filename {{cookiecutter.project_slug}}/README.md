# {{cookiecutter.project_name}}

{{ cookiecutter.description }}

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

{%- if cookiecutter.open_source_license != "Not open source" %}

License: {{cookiecutter.open_source_license}}
{%- endif %}

## Techstack

- Python 3.11
- Django
- Postgres {{ cookiecutter.postgresql_version }}
  {% if cookiecutter.use_celery == "y" %}
- Celery
- Cache & Broker: Redis
  {% else %}
- Cache: Redis
  {% endif %}
- Pre-commit
- Docs: Sphinx

## First Steps after creating the project with cookiecutter

### If you are NOT using docker:

1. ``cd`` into the created project folder or open it in your IDE
2. create and activate a new virtual environment and install the requirements
   1. `virtualenv venv`
   2. ``venv\Scripts\activate`` for windows or ``source venv/bin/activate`` for linux
   3. `pip install -r requirements/local.txt`
3. Optionally create a new ``.env`` file

### If you are using docker:

1. Ensure pre-commit is installed on your base python interpreter
   1. Install pre-commit with `pip install pre-commit`

### Both:

1. Git init and add the remote repository. These steps are usually shown on the empty repository page on Gitlab
    - Run git init `git init --initial-branch=main`
    - Add gitlab origin `git remote add origin {{ cookiecutter.repository_url }}`
    - Add all files `git add .`
    - Install pre-commit hooks with `pre-commit install`
    - Run commit `git commit -m "Initial commit"`
    - Run push `git push --set-upstream origin main`

**!!!Delete this section after you have completed the steps above!!!**

## Local Setup if you dont use docker

1. Create a virtual environment using python 3.11
2. Activate the virtual environment
3. Install the requirements with `pip install -r requirements/local.txt`
4. Create a new ``.env`` file and copy the content from ``.env.example`` into it
5. Create a new postgres database and add the credentials to the ``.env`` file
6. Run the migrations with `python manage.py migrate`
7. Create a new superuser with `python manage.py createsuperuser`
8. Run the development server with `python manage.py runserver`

## Local Setup if you use docker

**Prerequisites:**

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

1. Env-Files are located in the ``.envs/.local/`` directory. You can copy the content from ``.envs/.local/.env.example``
   into a new file ``.envs/.local/.env`` and adjust the values if needed. More information about configuring the
   environment [here.](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html#configuring-the-environment)
2. Run the stack using ``docker compose -f local.yml up``. This builds the images and starts the containers.
3. Any shell command like Management commands must be done using the ``docker compose -f local.yml run --rm`` command,
   for example:
    - ``docker compose -f local.yml run --rm django python manage.py migrate``
    - ``docker compose -f local.yml run --rm django python manage.py createsuperuser``
4. Pre-commit is done outside the containers. To run `pre-commit install ` use the global interpreter from the cmd.

See more about developing locally with
docker [here.](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html)

### Tips for PyCharm users:

A few run configurations are already set up, for example ``compose up django`` and ``compose up docs``. You can use them
by clicking on the green play button in the top right corner of the IDE. Alternatively, open the ``local.yml`` file and
click on the green play on the left side of the file next to the ``services`` section.

**Configuring the interpreter:** You should also configure the docker-compose stack as a remote interpreter.

1. To do that, go the interpreter options and select "Add Python Interpreter" -> "Docker Compose". Select
    - Server: Docker
    - Configuration files: Path to the docker-compose file, usually `./local.yml`
    - Service: Django
2. Click next, the containers will be started (and optionally built). After that, click next again.
3. Select an interpreter from the running container. If no option is available, the container might have failed to
   start. Try to restart the PyCharm IDE then.

## Pre-commit

We use [pre-commit](https://pre-commit.com/) to ensure that all code is formatted correctly and that there are no
linting errors. You can install the pre-commit hooks with `pre-commit install`. This will install the pre-commit hooks
for this repository. If you want to run the pre-commit hooks manually you can run `pre-commit run --all-files`.
See ``.pre-commit-config.yaml`` for more information.

## Staging Deployment

The application will be automatically deployed to a subdomain of
our [staging environment](https://v2.singular-it-test.de) when you push to the `main` branch.
The subdomain is based on the repository and group name. You can find the url at the end of the deployment log in the
gitlab ci/cd pipeline.

If you deploy for the first time make sure that you set the following variables in the gitlab ci/cd settings (go
to `Settings -> CI/CD -> Variables`):

- `DJANGO_SECRET_KEY`
    - Environments: `main` (defaults to `main` or the specified branch name in the .gitlab/deploy.gitlab-ci.yml)
    - Check "Mask variable"
    - Uncheck "Expand variable reference"
    - Key: ``DJANGO_SECRET_KEY``
    - Value: _a_new_created_secret_key

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "
  Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into
  your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar),
so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy {{cookiecutter.project_slug}}

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

{%- if cookiecutter.use_celery == "y" %}

### Celery

This app comes with Celery.

To run a celery worker:

```bash
cd {{cookiecutter.project_slug}}
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important _where_ the celery commands are run. If you are in the
same folder with _manage.py_, you should be right.

To run [periodic tasks](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html), you'll need to start the
celery beat scheduler service. You can start it as a standalone process:

```bash
cd {{cookiecutter.project_slug}}
celery -A config.celery_app beat
```

or you can embed the beat service inside a worker with the `-B` option (not recommended for production use):

```bash
cd {{cookiecutter.project_slug}}
celery -A config.celery_app worker -B -l info
```

{%- endif %}
{%- if cookiecutter.use_mailpit == "y" %}

### Email Server

{%- if cookiecutter.use_docker == "y" %}

In development, it is often nice to be able to see emails that are being sent from your application. For that reason
local SMTP server [Mailpit](https://github.com/axllent/mailpit) with a web interface is available as docker container.

Container mailpit will start automatically when you will run all docker containers.
Please
check [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html)
for more details how to start all containers.

With Mailpit running, to view messages that are sent by your application, open your browser and go
to `http://127.0.0.1:8025`
{%- else %}

In development, it is often nice to be able to see emails that are being sent from your application. If you choose to
use [Mailpit](https://github.com/axllent/mailpit) when generating the project a local SMTP server with a web interface
will be available.

1. [Download the latest Mailpit release](https://github.com/axllent/mailpit/releases) for your OS.

2. Copy the binary file to the project root.

3. Make it executable:

       $ chmod +x mailpit

4. Spin up another terminal window and start it there:

       ./mailpit

5. Check out <http://127.0.0.1:8025/> to see how it goes.

Now you have your own mail server running locally, ready to receive whatever you send it.

{%- endif %}

{%- endif %}
{%- if cookiecutter.use_sentry == "y" %}

### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account
at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.
{%- endif %}

## Deployment

The following details how to deploy this application.
{%- if cookiecutter.use_heroku.lower() == "y" %}

### Heroku

See
detailed [cookiecutter-django Heroku documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html).

{%- endif %}
{%- if cookiecutter.use_docker.lower() == "y" %}

### Docker

See
detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

{%- endif %}
{%- if cookiecutter.frontend_pipeline in ['Gulp', 'Webpack'] %}

### Custom Bootstrap Compilation

The generated CSS is set up with automatic Bootstrap recompilation with variables of your choice.
Bootstrap v5 is installed using npm and customised by tweaking your variables in `static/sass/custom_bootstrap_vars`.

You can find a list of available
variables [in the bootstrap source](https://github.com/twbs/bootstrap/blob/v5.1.3/scss/_variables.scss), or get
explanations on them in the [Bootstrap docs](https://getbootstrap.com/docs/5.1/customize/sass/).

Bootstrap's javascript as well as its dependencies are concatenated into a single file: `static/js/vendors.js`.
{%- endif %}
