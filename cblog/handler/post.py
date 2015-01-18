#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from tornado.gen import coroutine

from . import BaseHandler
from cblog.app.web import post as post_base


class PostHandler(BaseHandler):

    def get(self, post_id):
        post = post_base.get(post_id, count_pv=True)
        self.write(post)

    def post(self):
        title = self.get_argument('title', None)
        content = self.get_argument('content', None)
        status = self.get_argument('status', None)
        category_id = self.get_argument('category_id', None)
        tag = self.get_argument('tag', None)

        post_base.add(title, content, status, category_id, tag)

    def put(self, post_id):
        title = self.get_argument('title', None)
        content = self.get_argument('content', None)
        status = self.get_argument('status', None)
        category = self.get_argument('category', None)

        post_base.update(post_id, title, content, status, category)

    def delete(self, post_id):
        post_base.delete(post_id)
