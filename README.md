# mawi-test-task-first

> An API Django project for collecting electrocardiogram signals and their processing.

## Project structure

    mawi-test-task-first/
    ├── mawi_test_task_first
    └── ecg_handler

The 2 root level folders separate the **project folder** (mawi_test_task_first) and the **app folder** (ecg_handler).

The root level folder contains the following files:

    mawi_test_task_first/
    ├── manage.py
    └── requirements.txt

### mawi_test_task_first folder

The content:

    mawi_test_task_first/
    ├── __init__.py
    ├── celery.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

* **__init__.py:** an empty file that tells Python that this folder should be considered a Python package.
* **celery.py:** instantiates a Celery instance.
* **channels_authentication.py:** a middleware for custom token-based authorization for Channels.
* **routing.py:** a root routing configuration for Django Channels.
* **settings.py:** settings/configuration for the project.
* **urls.py:** the root URL declarations for the project.
* **wsgi.py:** an entry-point for WSGI-compatible web servers to serve the project.

### ecg_handler app

The app contains models, views, tasks, etc for collecting electrocardiogram signals and their processing.

The app's folder structure:

    ecg_handler/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── consumers.py
    ├── models.py
    ├── routing.py
    ├── tasks.py
    ├── views.py
    ├── urls.py
    └── tests.py

The structure is typical for a Django app, but I want pay attention on some files:

* **consumers.py:** contains class ElectrocardiogramConsumer. ElectrocardiogramConsumer is a WebSocket consumer, designed for sending the signals processing results to a client.
* **models.py:** contains mongoengine documents for storing of signals.
* **routing.py:** an app routing configuration for Django Channels.
* **tasks.py:** contains celery tasks for signals processing.

## Running the tests

Run the following command to start unit tests:
```console
python manage.py tests
```

* **ecg_handler/test.py** contains unit tests for clients app's API views

### Websocket

ecg_handler app contains a template - electrocardiogram.html for testing ElectrocardiogramConsumer.

## Built With

* [Django](https://www.djangoproject.com/) - a high-level Python Web framework.
* [Django REST framework](https://www.django-rest-framework.org/) - a powerful and flexible toolkit for building Web APIs.
* [Django Channels](https://channels.readthedocs.io/en/latest/) - a project that takes Django and extends its abilities beyond HTTP - to handle WebSockets, chat protocols, IoT protocols, and more.
* [Mongoengine](http://mongoengine.org/) - a Document-Object Mapper (think ORM, but for document databases) for working with MongoDB from Python.
* [Celery](http://www.celeryproject.org/) - an asynchronous task queue/job queue based on distributed message passing. 
* [Redis](https://redis.io) -  is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broker. 
