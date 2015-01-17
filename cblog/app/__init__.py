#!/usr/bin/env python2
# coding=utf8

from cblog.app.web import (
    IndexHandler,
    PostHandler,
)


handlers = [
    (r"/", IndexHandler),
    (r'/page/(\d+)', IndexHandler),
    (r'/post/(\d+)', PostHandler),
    (r'/post/new', PostHandler),
]
