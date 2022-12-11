# ГАДАНИЕ НА КАРТАХ ТАРО НЕДОРОГО 

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
