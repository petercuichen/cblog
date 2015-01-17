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
        post = post_base.get(post_id)
        self.write(post)

    def put(self, post_id):
        pass

    def delete(self, post_id):
        pass


routes = [
    (r"/", IndexHandler),
    (r'/page/(\d+)', IndexHandler),
]
