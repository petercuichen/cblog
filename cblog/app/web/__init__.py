#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from tornado.gen import coroutine
from tornado.web import RequestHandler

from cblog.app.web import post as post_base
from cblog.core.const import page_size
from cblog.model import Post


class IndexHandler(RequestHandler):

    def get(self, page_no=1):
        posts = post_base.query(
            status=Post.STATUS_PUBLISHED,
            offset=(page_no-1),
            limit=page_size,
        )
        self.write(posts)


class PostHandler(RequestHandler):

    def get(self, post_id):
        post = post_base.get(post_id, count_pv=True)
        self.write(post)

    def post(self, post_id):
        title = self.get_argument('title', None)
        content = self.get_argument('content', None)
        status = self.get_argument('status', None)
        category_id = self.get_argument('category_id', None)
        tag = self.get_argument('tag', None)

        post_base.add(title, content, status, category_id, tag)

    def put(self, post_id):
        title = self.get_argument('title')
        content = self.get_argument('content', None)
        status = self.get_argument('status', None)
        category = self.get_argument('category', None)

        post_base.update(post_id, title, content, status, category)

    def delete(self, post_id):
        post_base.delete(post_id)
