### Django Blog

> Add, Read but _NOT_ yet Delete and Update (They are coming soon)

#### Getting started

```Clone the repository```

Running the app

> Install all the requirements in your environment.


```pip install -r requirements.txt```

#### Setup the Database in the '''blog/settings.py'''

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD':'',
        'HOST':'',
        'PORT':''
    }
}
```

> After that, run the app using Django manage.py.

```
python manage.py runserver
```

> Access the homepage on '''http://localhost:8000'''


