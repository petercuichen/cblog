#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function


from tornado import gen
from tornado.httpclient import AsyncHTTPClient, HTTPClient


def asynchronous_fetch(url):
    http_client = AsyncHTTPClient()

    def handle_response(response):
        print(response.body)

    return http_client.fetch(url, callback=handle_response)


def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.body


@gen.coroutine
def fetch_coroutine(url):
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)
    return response.body


if __name__ == '__main__':
    # print(asynchronous_fetch('http://www.baidu.com'))
    # print(synchronous_fetch('http://www.baidu.com'))
    # print(fetch_coroutine())
