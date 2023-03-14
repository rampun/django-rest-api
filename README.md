# Django Rest API using ViewSets

A simple Django project with SQlite database connection and Rest API

## Usage

```
python3

# clone the project and follow the steps below
git clone git@github.com:rampun/django-rest-api.git

# cd to the project
cd django-rest-api

# create a virtual environment
python3 -m venv venv

# activate the virtual environment
. venv/bin/activate

# install the required packages inside venv
pip3 install -r requirements.txt

# if you need to upgrade pip for package compatibility please run the command below
# and install the require package again
pip3 install --upgrade pip

# start a project using django-admin
django-admin startproject drf .

# start an app using django-admin
django-admin startapp rest_api

# run the server
python3 manage.py runserver 8000

# make the migrations
python3 manage.py makemigrations

# migrate the tables
python3 manage.py migrate

# deactivate the virtual environment
deactivate
```
Access the project locally
http://localhost:8000/admin

Django Restframework
https://www.django-rest-framework.org/
