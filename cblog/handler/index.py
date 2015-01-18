#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function


#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from tornado.gen import coroutine

from . import BaseHandler
from cblog.app.web import post as post_base
from cblog.core.const import page_size
from cblog.models import Post


class IndexHandler(BaseHandler):

    def get(self, page_no=1):
        posts = post_base.query(
            status=Post.STATUS_PUBLISHED,
            offset=(page_no-1),
            limit=page_size,
        )
        results = [{'title': p.title,
                    'content': p.content,
                    'pv': p.pv,
                    'created_at': p.created_at.strftime('%Y-%m-%d')}
                   for p in posts]

        self.write({'posts': results})
