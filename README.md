# Notes

```curl
django-admin startproject [project-name]
```

- Project = the overall application
- Apps = could have multiple within one project (e-commerce shop, blog, etc.)
  - comes with a bunch of apps out of the box (admin, auth, contenttypes, etc.)

- Our routes are defined in 'urls.py'

### Start Dev Server
- don’t use this server in anything resembling a production environment. It’s intended only for use while developing. (We’re in the business of making Web frameworks, not Web servers.)

```curl
python manage.py runserver [optional-port-number]
```

- the 'You have 17 unapplied migration(s).' error is normal.

### Create an app

```curl
python manage.py startapp [app-name]
```

- make sure to add your apps to settings.py list

**What’s the difference between a project and an app?**

*An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.*

### Create migrations

```curl
python manage.py makemigrations polls
python manage.py migrate
```

*The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app*

*By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.*

*Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk. You can read the migration for your new model if you like; it’s the file polls/migrations/0001_initial.py*

To see what SQL that migration would run, run:

```curl
python manage.py sqlmigrate polls 0001
```

- We can play around with the free API Django gives us via an interactive Python shell. Run:
```curl
python manage.py shell
```
then,
```curl
from polls.models import Question,Choice
from django.utils import timezone
Question.objects.all() # no questions in the system at this point
q = Question(question_text="What is your favourite Python framework?", pub_date=timezone.now())
q.save() # save object to database
q = Question.objects.get(pk=1)
q.choice_set.create(choice_text="Django", votes=0)
q.choice_set.create(choice_text="Flask", votes=0)
```

- the above adds a question and three choices to our database (sqlite3)

### Setup admin user

```curl
python manage.py createsuperuser
```
- Go to: http://127.0.0.1:8000/admin/login/?next=/admin/
  - username is lukemackenzie
  - password is password

- Register models in polls > admin.py

### Using a global templates file (instead of app specific):
- add the below to 'settings.py' file

```python
'DIRS': [os.path.join(BASE_DIR, 'templates')],
```

- the directories within 'pollster' are our 'apps' (polls, pages)
<br>

- A **view** is a “type” of Web page in your Django application that generally serves a specific function and has a specific template.
- In Django, web pages and other content are delivered by views. Each view is represented by a Python function (or method, in the case of class-based views). Django will choose a view by examining the URL that’s requested (to be precise, the part of the URL after the domain name).

### To deploy (Heroku)

- pip install gunicorn
- pip freeze > requirements.txt 
- heroku create [app-name]
- add 'STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')' to 'settings.py'
- create a 'Procfile' with 'web: gunicorn pollster.wsgi'
  - 'web' = process type (will receive web traffic)
  - 'gunicorn' = command needed to run our web process
  - 'wsgi' = Web Service Gateway Interface
  - 'pollster' = name of directory that holds 'settings.py'