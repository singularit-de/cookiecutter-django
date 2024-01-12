SingularIT Customizations
=========================

This cookiecutter template comes with some customizations for SingularIT.

Changes and Removals
^^^^^^^^^^^^^^^^^^^^

In this section we describe the changes and removals we made to the original cookiecutter template.

Allauth
-------

We removed allauth from the template.


Github Actions and Issue templates
----------------------------------

We removed the Github Actions and Issue templates.

Pre-Commit
----------

We removed the pre-commit hook `prettier`.


Cookiecutter.json
-----------------

Editor
~~~~~~

We removed the selection of an editor, because usually more than one IDE is used in a team.


Open Source
~~~~~~~~~~~

We changed the order of the licenses to declare "Not Open Source" as the default.

Postgresql
~~~~~~~~~~

We removed the selection of an older version of Postgresql.

Cloudprovider
~~~~~~~~~~~~~

We changed the order of the cloudproviders to declare "None" as the default.

Mail Service
~~~~~~~~~~~~

We changed the order of the mail services to declare "Other SMTP" as the default.

Django Rest Framework
~~~~~~~~~~~~~~~~~~~~~

We changed the default usage of Django Rest Framework to "yes".

Frontend Pipeline
~~~~~~~~~~~~~~~~~

We changed the order of the frontend pipelines to declare "None" as the default.

Django Whitenoise
~~~~~~~~~~~~~~~~~

We changed the default usage of Django Whitenoise to "yes". Usually whitenoise is used for the django admin panel in production.


CI Tool
~~~~~~~

We changed the order of the CI tools to declare "Gitlab" as the default.

Keep Local Envs in VCS
~~~~~~~~~~~~~~~~~~~~~~

We changed the default usage of keeping local envs in VCS to "no".


Gitignore
---------

We added a custom section in the gitignore file.


Utility Files
-------------

We remove the utility files in the root directory in the `post_gen_project.py` hook, because we don't need them.

Languages
---------

We removed the language `fr_FR` and `pt_BR` from the `locale` directory, because we usually dont have customers from these countries.

Additions
^^^^^^^^^

In this section we describe the additions we made to the original cookiecutter template.

cookiecutter.json
------------------

repository_url
~~~~~~~~~~~~~~

We added a `repository_url` variable to the `cookiecutter.json` file. This variable is used in the ``README.md`` file
for initial git steps.

Gitlab CI
---------

We implemented a pipeline for the main branch. This includes:

1. pre-commit
2. tests with pytest
3. A deployment to our staging server on singular-it-test.de

Read more about in the `README.md > Staging Deployment` in the generated project.

`env.example`
-------------
We added an `env.example` file to the project.

Config Settings Static Files
----------------------------

We added a custom `static_files.py` to the config settings. This file is used for docker build stages.

`commons` package
-----------------

We added a `commons` package to the django app. This package contains common code for all apps in the project.
