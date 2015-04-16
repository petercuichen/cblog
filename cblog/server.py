#!/usr/bin/env python2
# coding=utf8

from jinja2 import Environment, FileSystemLoader
import tornado.ioloop
import tornado.web
from cblog import config
from cblog.core import (
    db,
    session,
)
from cblog.url import handlers


jinja_environment = Environment(
    loader=FileSystemLoader(config.WEB['template_path']),
    auto_reload=config.WEB['debug'],
    autoescape=config.WEB['autoescape'],
)


class Application(tornado.web.Application):

    def __init__(self):

        tornado.web.Application.__init__(self, handlers, **config.WEB)

        self.jinja_env = jinja_environment

        self.session_store = session.RedisSessionStore(db.redis)

        # self.email_backend = smtp_server
        # TODO in near future

        print('CBlog is successfully started.')

app = Application()


if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
