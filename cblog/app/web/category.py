#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from cblog.core.db import DBSession, db_commit
from cblog.core.exc import PostExc
from cblog.model import Category


@db_commit
def add(category_name):
    new_category = Category(name=category_name)
    DBSession().add(new_category)


@db_commit
def query():
    return DBSession().query(Category).all()


@db_commit
def update(category_id, category_name):
    category = DBSession().query(Category).get(category_id)

    if not category:
        raise PostExc('Category with id {} is not exist.'.format(category_id))

    category.name = category_name


@db_commit
def delete(category_id):
    DBSession().query(Category).get(category_id).delete()
