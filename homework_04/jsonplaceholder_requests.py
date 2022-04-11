"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio

import aiohttp

import ujson as ujson
from loguru import logger

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str) -> dict:
    logger.info("fetch url {}", url)
    async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
        async with session.get(url) as response:
            logger.info("fetched url {} and got data {}", response.url, response)
            return await response.json(loads=ujson.loads)


async def async_fetch_users() -> dict:
    return await fetch_json(USERS_DATA_URL)
    # users = []
    # for user in fetched_users:
    #     items = user.items()
    #     new_item = {}
    #     for key, value in items:
    #         if key in "id" or key in "name" or key in "username" or key in "email":
    #             new_item[key] = value
    #     users.append(new_item)
    # logger.info("parsed users {}", users)
    # return users


async def async_fetch_posts() -> dict:
    return await fetch_json(POSTS_DATA_URL)


async def task():
    await async_fetch_posts()
    await async_fetch_users()
    await fetch_json(USERS_DATA_URL)


if __name__ == '__main__':
    # asyncio.run(fetch_json(USERS_DATA_URL))
    # asyncio.run(async_fetch_users())
    asyncio.get_event_loop().run_until_complete(task())
