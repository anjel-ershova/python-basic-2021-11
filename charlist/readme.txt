создать новый проект джанго
django-admin startproject <project name>

запустить тестовый сервер джанго (из корня, оттуда, где файл manage.py)
python manage.py runserver

для админки:
python manage.py createsuperuser

создать приложение:
django-admin startapp <app name> --> занести в <название проекта> --> settings --> INSTALLED_APPS

миграции:
python manage.py makemigrations - создает заготовку под миграции
python manage.py migrate - непосредственно мигрирование

модели
если достаточно информации только о самой модели - методы пишутся в классе самой модели (работа с model instance)
если нужно знание о нескольких сущностях, то используется model manager

запуск тестов
python manage.py test - юниттесты
pytest