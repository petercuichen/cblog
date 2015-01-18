#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import os


WEB = {
    'debug': True,
    'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'cookie_secret': "NjAzZWY2ZTk1YWY5NGE5NmIyYWM0ZDAzOWZjMTg3YTU=|1355811811|3245286b611f74805b195a8fec1beea7234d79d6",
    'login_url': '/account/login',
    "xsrf_cookies": True,
    'autoescape': None
}

MYSQL = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'pwd': '',
    'database': 'cblog'
}


REDIS = {
    "host": "127.0.0.1",
    "port": 6379,
    "password": "",
}
