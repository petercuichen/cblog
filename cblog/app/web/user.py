#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from cblog.core.db import DBSession
from cblog.models import User


def get(name):
    return DBSession.query(User).filter(User.name == name).first()


def check_pwd(user):
    return DBSession().query(User).\
        filter(User.password == user.password).\
        filter(User.is_admin == 1).first() is not None
