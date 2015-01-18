#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import (
    Column,
    DateTime,
    UnicodeText,
    Integer,
    String,
    SmallInteger)

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(SmallInteger, default=0)
    email = Column(String, default='')
    last_login = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Post(Base):
    __tablename__ = 'post'

    STATUS_DRAFT = 0
    STATUS_PUBLISHED = 1
    STATUS_PRIVATE = 2
    STATUS_DELETED = -1

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, nullable=False)
    title = Column(String, default='')
    category_id = Column(Integer, default=-1)
    pv = Column(Integer, default=0)
    status = Column(SmallInteger, default=STATUS_DRAFT)
    content = Column(UnicodeText, default=u'')
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    post_id = Column(Integer, nullable=False)

