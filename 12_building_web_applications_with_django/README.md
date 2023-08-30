## install django:

```bash:
mkdir vidly
cd vidly
pipenv install django==2.1
```


## activate virtual environment:
`pipenv shell`

## create a new django project:
`django-admin startproject vidly .`

## start development server on port 8000:
`python3 manage.py runserver`

## start an app:
django project is composed of several apps that support specific functions that can be reused in other websites (projects).

`python3 manage.py startapp movies`



