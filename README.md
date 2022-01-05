# Тестовое задание "Населённые пункты Московской области"

Для скачивания проекта и установки зависимостей выполнить:

```shell
git clone https://github.com/tivewsalaeharad/test_django.git
cd test_django
pip install -r requirements.txt
```

Для создания и заполнения базы данных выполнить:

```shell
cd moscowregion
python manage.py makemigrations
python manage.py migrate
python manage.py parsecities
```