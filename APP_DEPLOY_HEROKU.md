# Python Heroku Deployment

> Steps to create a postgres database and deploy this Python app to Heroku

### Install guinicorn locally
```
pipenv install gunicorn
or
pip install gunicorn
```

### Install Heroku CLI
https://devcenter.heroku.com/articles/heroku-cli

### Login via CLI
```
heroku login
```
### Create app
```
heroku create appname
```
create two apps: one for the website and another one for the database

### Create database
```
heroku addons:create heroku-postgresql:hobby-dev --app appname
```
create one for database

### Get URI
```
heroku config --app appname

# Add to your app
```

### Create Procfile
```
touch Procfile

# Add this
web: gunicorn app:app
```

### Create requirements.txt
```
pip freeze > requirements.txt
```

### Create runtime.txt
```
touch runtime.txt

# Add this
python-3.8
```

### Deploy with Git
```
git init
git add . && git commit -m 'Deploy'
heroku git:remote -a appname
git push heroku master
```

### Add table to website remote database
go to chatbot.py and make sure the greetings.yml training line is not commented
on terminal, type:
```
heroku run python --app appname
>>> from app import *
>>>exit()
```

### Prepare Database
```
comment the big training list (chatbot.py,lines 48-53)
decomment the "greetings.yml" training line (line 45)
follow 'add table' instructions above (use the app where app.py's stored, not the database)
go to your database, alter table properties: (tested using pgadmin4)
statement:length/precision of text,search_text,in_response_to,search_in_response_to to 1,000
statement:length/precision of conversation,persona to 100
tag: length/precision of name to 100
decomment the big training list (lines 48-53)
comment the greetings training line (line 45)
follow 'add table' instructions above
comment both training lists 
```

### Visit app
```
heroku open
```
