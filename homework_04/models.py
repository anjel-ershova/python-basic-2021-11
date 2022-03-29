"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey, Text,
)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, declared_attr

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://user:password@localhost:5433/postgres"
engine = create_async_engine(PG_CONN_URI, echo=True)


class Base:

    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"{self.__class__.__name__}, id={self.id}"


Base = declarative_base(bind=engine, cls=Base)

Session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


class User(Base):
    name = Column(String(32))
    username = Column(String(32), unique=True)
    email = Column(String(32), unique=True)

    posts = relationship("Post", back_populates="user")

    def __init__(self, id, name, username, email):
        self.id = id
        self.name = name
        self.username = username
        self.email = email

    def __repr__(self):
        return f"name={self.name!r}, username={self.username}, email={self.email!r})"


class Post(Base):
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(Text)
    body = Column(Text)

    user = relationship("User", back_populates="posts")

    # алхимия умеет работать и без __init__ - берет за структуру данные колонок
    # def __init__(self, user_id, title, body):
    #     self.user_id = user_id
    #     self.title = title
    #     self.body = body

    def __repr__(self):
        return f"userId={self.user_id!r}, title={self.title!r}, body={self.body!r}"
