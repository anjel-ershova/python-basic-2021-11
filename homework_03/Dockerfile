# билд docker build . -t blogapp (-t blogapp - просто имя контейнера)
# запуск: docker run -p 8003:8000 --name=anjel_app --rm blogapp
#(-p 8003:8000 - мне нужен локально 8000 порт свободным, поэтому, мапплю на 8003 порт,
#--name=anjel_app имя - просто для красоты,
#-- rm - чтобы не плодились однотипные контейнеры, очищает все контейнеры с таким именем после запуска очередного)
# docker stop <container id>, взять id можно из docker ps

FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD uvicorn app.app:app --host=0.0.0.0 --port=8000
