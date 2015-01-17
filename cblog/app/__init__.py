#!/usr/bin/env python2
# coding=utf8
from tornado.web import url
from cblog.app.main import MainHandler


handlers = [
    url(r"/", MainHandler),
]
