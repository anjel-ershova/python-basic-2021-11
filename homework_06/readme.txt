перед запуском фласка:
set FLASK_APP=app.py
set FLASK_ENV=development

запуск Flask:
flask run --port=xxxx
или
python app.py, но при таком запуске в app должен быть блок
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=xxxx)

погасить Flask app:
ctrl + C

 миграции:
# flask db init - инициализировать работу с миграциями
# flask db migrate -m "Migration theme" - подготовить миграцию (в версиях ее найти и проверить, что все ок)
# flask db upgrade - выполнить подготовленную миграцию

собрать контейнер:
docker-compose build <service name>

запуск докера
docker-compose up -d <service name> # -d - в режиме демона, в фоне, работает и с закрытой консолью
docker-compose up --build <service name> - сразу и собрать и запустить контейнер