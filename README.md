### Notes
- Remember that the entire repo is the Django 'project' (client-portal, in this case.)
- A Django project can contain more than one app (polls is an app_name, for example.)

### Create a new app
`django-admin startproject <app_name> <project_name>`

### Run server
`python3 manage.py runserver`

### Run tests
`python3 manage.py test <app_name>`

### If making changes to models
`python3 manage.py makemigrations <app_name>`