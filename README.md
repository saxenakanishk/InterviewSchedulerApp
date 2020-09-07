# InterviewSchedulerApp
Simple app to schedule interviews

## Requirements
1. Python 3.6
2. SQLite3 [Here](https://www.sqlite.org/download.html)
3. Recommend SQLite browser [Available](https://sqlitebrowser.org/)

## Setup
1. Install flask and packages

```
$ pip install flask
$ pip install flask-wtf
$ pip install flask-sqlalchemy
$ pip install flask-migrate
$ pip install flask-login
```

2. Define the project

```
$ export FLASK_APP=lab2.py
```

3. Init the database

```
$ flask db init
```

## Migrating data

1. Run the migration command to create tables

```
$ flask db upgrade
```

2. Populate the database with dummy data

```
python populate.py
```

## Running
1. Run the flask application from the project directory, running on localhost

```
$ flask run
```

2. Open the app in browser: [localhost](http://127.0.0.1:5000/)