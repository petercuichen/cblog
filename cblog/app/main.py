#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import time

from tornado.gen import coroutine
from tornado.web import RequestHandler


class MainHandler(RequestHandler):
    @coroutine
    def get(self):
        yield self.write('<html><body><form action="/" method="POST">'
                         '<input type="text" name="message">'
                         '<input type="submit" value="Submit">'
                         '</form></body></html>')
        time.sleep(5)

    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_body_argument("message"))

