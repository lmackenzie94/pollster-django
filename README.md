# Notes

```curl
django-admin startproject [project-name]
```

- Project = the overall application
- Apps = could have multiple within one project (e-commerce shop, blog, etc.)
  - comes with a bunch of apps out of the box (admin, auth, contenttypes, etc.)

- Our routes are defined in 'urls.py'

```curl
python manage.py runserver 
```

- the 'You have 17 unapplied migration(s).' error is normal.

### Create an app

```curl
python manage.py startapp [app-name]
```

- make sure to add your apps to settings.py list

### Create migrations

```curl
python manage.py makemigrations polls
python manage.py migrate
```

- to access/manipulate data from the shell, run:
```curl
python manage.py shell
```
then,
```curl
from polls.models import Question,Choice
from django.utils import timezone
q = Question(question_text="What is your favourite Python framework?", pub_date=timezone.now())
q.save()
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

### To deploy

- pip install gunicorn
- pip freeze > requirements.txt 