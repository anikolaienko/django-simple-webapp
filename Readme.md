# Django Simple WebApp

Simplistic web application written in Python3 using Django framework.

I have spent quite some time learning and practicing Algorithms, Data Structures, System Design,Distributed Systems, Operating Systems, preparing to FAANG interviews. This is my come back to web development.

If you are interested in my profile, find more information about me on [andnik.com](http://andnik.com)

## Deploy on dev environment
* Install `virtualenv`: `pip install virtualenv`
* Create virtual environment: `virtualenv -p 3.8 .venv`
* Run virtual environment: `. ./.venv/bin/activate`
* Install requirements: `pip install -r requirements.txt`
* Run migrations: `./manage.py migrate`
* Seed test data: `./manage.py load_data initial_data`
* Run dev server: `./manage.py runserver`

## Run tests
```
./manage.py test polls
```

## Check coverage
```
coverage run --source='polls' manage.py test poll
coverage report
```