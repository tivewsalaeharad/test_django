# Тестовое задание "Населённые пункты Московской области"

Для скачивания и первоначальной настройки проекта выполнить:

```shell
git clone https://github.com/tivewsalaeharad/test_django.git
cd test_django
python -m venv venv
venv\Scripts\activate
```

Консоль перейдёт в режим локального окружения. Для установки зависимостей выполнить:

```shell
pip install -r requirements.txt
```

Для создания и заполнения базы данных выполнить:

```shell
cd moscowregion
python manage.py makemigrations
python manage.py migrate
python manage.py parsecities
```