
https://docs.docker.jp/compose/django.html
https://qiita.com/A-Kira/items/f401aea261693c395966

https://qiita.com/bakupen/items/f23ce3d2325b4491a2ddhttps://qiita.com/bakupen/items/f23ce3d2325b4491a2dd
  # dbとwebの接続がうまくいかなかったが、この記事のようにwebをrestartしたらいけるようになった


Dockerfile # docker buildでイメージを作成する
```
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
```

requirements.txt #イメージ内で必要なモジュールをインストールする
```
Django==3.1.4
mysqlclient
```

docker-compose.yml
```
version: '3'

services:
  db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: Password1!
      MYSQL_DATABASE: epic7
      MYSQL_USER: norden
      MYSQL_PASSWORD: Password1!
      TZ: 'Asia/Tokyo'
    command: mysqld --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
    ports:
    - 3306:3306
  web:
    build: .
    command: python3 manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
```

docker-compose run web django-admin.py startproject composeexample .
WARNING: Image for service web was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.

sudo chown -R $USER:$USER .

code composeexample/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'epic7',
        'USER': 'norden',
        'PASSWORD': 'Password1!'
        'PORT': 3306,
    }
}


docker-compose up

https://qiita.com/bakupen/items/f23ce3d2325b4491a2ddhttps://qiita.com/bakupen/items/f23ce3d2325b4491a2dd
  # dbとwebの接続がうまくいかなかったが、この記事のようにwebをrestartしたらいけるようになった


ブラウザアクセスるとエラー
‘‘‘
DisallowedHost at /
Invalid HTTP_HOST header: '140.238.63.114:8000'. You may need to add '140.238.63.114' to ALLOWED_HOSTS.
‘‘‘‘‘‘

settings.py
```
DEBUG = True
ALLOWED_HOSTS = ['140.238.63.114']
```

### app
https://docs.djangoproject.com/ja/3.1/intro/tutorial01/

docker-compose run web python3 manage.py startapp polls


### error 
```
[opc@centos7 docker-django]$ python manage.py migrate
  File "manage.py", line 17
    ) from exc
```
https://teratail.com/questions/149773
python3で打つべきか？

‘‘‘
[opc@centos7 docker-django]$ python3 manage.py migrate
Traceback (most recent call last):
  File "manage.py", line 11, in main
    from django.core.management import execute_from_command_line
ModuleNotFoundError: No module named 'django'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "manage.py", line 22, in <module>
    main()
  File "manage.py", line 17, in main
    ) from exc
ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?
‘‘‘

dockerだからかな。とりあえずスルー

### model

docker exec -it *** /bin/bash
python manage.py ***

python manage.py migrate
root@b827ac5e27b3:/code# python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying polls.0001_initial... OK
root@b827ac5e27b3:/code# 

### api

python manage.py shell

from polls.models import Choice, Question
Question.objects.all()

from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
q.id
q.question_text
>>> q.question_text
"What's new?"

q.pub_date
>>> q.pub_date
datetime.datetime(2020, 12, 15, 6, 2, 55, 277103, tzinfo=<UTC>)

q.question_text = "What's up?"
q.save()  

Question.objects.all()
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>

__str__をmodelに追加することでメッセージを変更可能

from polls.models import Choice, Question
from django.utils import timezone
current_year = timezone.now().year

Question.objects.all()
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

Question.objects.filter(id=1)
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>

Question.objects.filter(question_text__startswith='What')
>>> Question.objects.filter(question_text__startswith='What')
<QuerySet [<Question: What's up?>]>

Question.objects.get(pub_date__year=current_year)
Question.objects.get(id=2)

### 管理ユーザーの作成
https://docs.djangoproject.com/ja/3.1/intro/tutorial02/

python manage.py createsuperuser
root@b827ac5e27b3:/code# python manage.py createsuperuser
Username (leave blank to use 'root'): 
Email address: nordengames2018@gmail.com
Password: Take@5534
Password (again): Take@5534
Superuser created successfully.