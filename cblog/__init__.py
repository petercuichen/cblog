#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function


import tornado.web
from cblog.app import handlers


application = tornado.web.Application(
    handlers=handlers,
    autoreload=True
)
