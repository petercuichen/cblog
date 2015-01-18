#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
from cblog.handler.account import (
    LoginHandler,
    LogoutHandler,
)
from cblog.handler.index import IndexHandler
from cblog.handler.post import PostHandler


handlers = [
    (r"/", IndexHandler),
    (r'/page/(\d+)', IndexHandler),

    (r'/post/(\d+)', PostHandler),
    (r'/post/new', PostHandler),

    (r'/account/login', LoginHandler),
    (r'/account/logout', LogoutHandler),

    # (r'/admin/(\d+)', ),
    # (r'/admin/new', ),

]
