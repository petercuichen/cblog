#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from cblog.core.const import max_query_size
from cblog.core.db import DBSession, db_commit
from cblog.core.exc import PostExc
from cblog.model import Post
from cblog.app.web import tag as tag_base
# from xxx import current_user


def get(post_id, count_pv=False):
    post = DBSession().query(Post).get(post_id)

    if not post:
        raise PostExc('Post with id {} is not exist.'.format(post_id))

    if count_pv:
        incre_pv(post.id)

    return post


@db_commit
def incre_pv(post_id):
    post = DBSession().query(Post).get(post_id)
    if post:
        post.pv += 1


def query(category_id=None, status=None, tag=None, offset=0, limit=20):
    session = DBSession()
    q = session.query(Post)

    if category_id is not None:
        q = q.filter(Post.category_id == category_id)

    if status is not None:
        q = q.filter(Post.status == status)

    if tag is not None:
        q = q.filter(Post.tag == tag)

    if offset is not None:
        q = q.offset(offset)

    if limit is not None:
        q = q.limit(min(limit, max_query_size))

    return q.all()


@db_commit
def add(title, content, status=Post.STATUS_DRAFT, category_id=-1, tag=''):
    session = DBSession()
    new_post = Post(
        author_id=-1,#current_user.id,
        title=title,
        content=content,
        status=status,
        category_id=category_id,
    )
    session.add(new_post)
    session.flush()

    if tag:
        tag_base.add(tag, new_post.id)

    return new_post.id


@db_commit
def update(post_id, title=None, content=None, status=None, category_id=None):

    post = get(post_id)

    if title is not None:
        post.title = title
    if content is not None:
        post.content = content
    if status is not None:
        post.status = status
    if category_id is not None:
        post.category_id = category_id


@db_commit
def delete(post_id):
    session = DBSession()
    post = session.query(Post).get(post_id)

    if not post:
        raise PostExc('Delete Error! Post with id {} is not exist.'
                      .format(post_id))

    # Do not actually delete the post
    post.status = Post.STATUS_DELETED
