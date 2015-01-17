#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function


class BaseExc(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class PostExc(BaseExc):
    pass

