#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from cblog.core.db import DBSession, db_commit
from cblog.model import Tag


@db_commit
def add(tag_name, post_id):
    post_tag = Tag(name=tag_name, post_id=post_id)
    DBSession().add(post_tag)


@db_commit
def delete(tag_name, post_id):
    DBSession().query(Tag).\
        filter(Tag.name == tag_name).\
        filter(post_id=post_id).delete()
