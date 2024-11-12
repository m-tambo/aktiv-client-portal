## Developing locally
Git clone this repo. Create/activate virtal env and pip install dependencies.

```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```


### Run server
`$ python3 manage.py runserver`


### Create a new app within project
`$ django-admin startproject <app_name>` from within root dir.


### Run tests
`$ python3 manage.py test <app_name>`


### After making changes to models
```
$ python3 manage.py makemigrations <app_name>
$ python3 manage.py migrate
```


### After pip installing any new pkgs
```
$ pip freeze > requirements.txt
```




## Notes
- Remember that the entire repo is the Django 'project' (client-portal, in this case.)
- A Django project can contain more than one app (polls is an app_name, for example.)
- - Django docs https://docs.djangoproject.com/en/5.1/


