#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from functools import wraps
from redis import Redis

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import scoped_session, sessionmaker

from cblog import config

########
# MySQL
########
engine = create_engine(
    "mysql+pymysql://{user}:{pwd}@{host}:{port}/{database}?charset=utf8".
    format(**config.MYSQL),
    pool_size=10,
    max_overflow=-1,
    pool_recycle=1800
)

DBSession = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine))


def db_commit(func):
    """ database session commit decorator """

    @wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        session = DBSession()
        # tmp
        # session._model_changes = {}
        try:
            session.commit()
        except SQLAlchemyError as se:
            session.rollback()
        finally:
            session.close()
        return ret

    return wrapper


########
# Redis
########
redis = Redis(**config.REDIS)

