# Django Learning

## **Day 1: Introduction to Django**

- It is a Python framework used to create websites using python.
- especially helpful for database driven websites.
- It emphasizes reusability of components, comes with ready-to-use features like login system, database connection and CRUD (Create Read Update Delete) operations.
- In Django there are primary command-line tools like `django-admin` and `manage.py` file.

## How Django works

- It follows the MVT (Model View Template) design pattern.
    1. Model
    2. View
    3. Template

## How to create the project

`django-admin startproject projectname .`

**Note**: here `.` is used to install the project in the current directory.

when the command runs, directory (project structure) and initial files should look like this:
```
manage.py
projectname/
    __init__.py
    settings.py
    urls.py
    wsgi.py
    asgi.py
```

## How to verify the project

Below command is used to run the built-in server which ensure that everything is wired correctly

`python manage.py runserver`

## Purpose of key files and directories

1. Root files:
    - `manage.py`
        - this is like remote control
        - rarely edit file
        - used in terminal to perform tasks like creating database, making migrations, and running the server

    - `db.sqlite3`
        - created after first migration
        - default development database
        - lightweight database

2. Configuration folder(`practice/`):
    - `settings.py`
        - most edited file in a new project, because it controls:
            - `INSTALLED_APPS`:
                - list of all the features/modules which is project uses
            
            - `DATABASE`:
                - conection details for your data storage

            - `TEMPLATES`:
                - instructions on how to render HTML

            - `STATIC_URLS`:
                - where CSS, JS, and images live

    - `urls.py`
        - this is like table of content
        - when a specific request is coming through browser, at that time Django look at that file and decide wihch piece of code should handle that specific request

    - `wsgi.py` and `asgi.py`
        - these are like gatekeepers of the web server
        - WSGI(Web Server Gateway Interface) is the standard for synchronous Python web apps.
        - ASGI(Asynchronous Server Gateway Interface) is used when modern features like WebSockets or async tasks are used.

3. Project's main application:
    - it is a specific module *ex.* a home page, a contact form, or a database
    - it hold's logic, models and views
    - a project can have many application
    - need to give a path/location where we want to store the app, after giving location run the below command for creating an app:
            
        `python3 manage.py startapp app_name`