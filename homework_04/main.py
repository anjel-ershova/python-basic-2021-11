"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
import sys

from loguru import logger
from sqlalchemy import MetaData

from jsonplaceholder_requests import async_fetch_users, async_fetch_posts
from models import Base, User, Post, Session, engine

metadata = MetaData()


async def create_schemas():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def async_create_users_and_posts():
    users_data, posts_data = await asyncio.gather(async_fetch_users(), async_fetch_posts())
    async with Session() as session:
        async with session.begin():  # await session.commit() отдельно не нужен, он есть в begin()
            for user in users_data:
                session.add(User(id=user['id'], name=user['name'], username=user['username'], email=user['email']))
            for post in posts_data:
                var = Post(id=post['id'], user_id=post['userId'], title=post['title'], body=post['body'])
                session.add(var)
                print(var.title)  # просто хотелось посмотреть, что происходит в цикле и записывается в базу


async def async_main():
    logger.info('delete and re-creation DB')
    await create_schemas()
    logger.info('DB created')

    logger.info('Create users and posts')
    await async_create_users_and_posts()
    logger.info('Users and posts created')


def main():
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
