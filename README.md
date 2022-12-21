[![Django CI](https://github.com/Shagulka/tarot-django/actions/workflows/django.yml/badge.svg)](https://github.com/Shagulka/tarot-django/actions/workflows/django.yml)
[![FLake8 CI](https://github.com/Shagulka/tarot-django/actions/workflows/flake8.yml/badge.svg)](https://github.com/Shagulka/tarot-django/actions/workflows/flake8.yml)

# ГАДАНИЕ НА КАРТАХ ТАРО НЕДОРОГО

Сайт с гаданием на картах Таро с помощью GPT-3

![image](image1.jpg)
![image](image2.jpg)

## фичи

- гадание на трех картах
- монетки чтобы покупать гадания
- даем монетки каждый день по серверному времени
- гадания с помощью GPT-3

## сделаем позже

- гадание на любое количество карт
- даем монетки каждый день по времени пользователя
- фронт по красоте

## set up the environment and install requirements

create .env file in the root directory of the project (optional)
```bash
cp .env.example .env
```

- ### windows

```ps
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
``` 

- ### unix

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```



## run the project

migration
```bash
python manage.py migrate
```

load fixtures (optional)
```bash
python manage.py loaddata initial.yaml
```

run server
```bash
python manage.py runserver
```
