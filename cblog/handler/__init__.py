#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function
import urllib
import tornado
from tornado.web import RequestHandler, HTTPError
from cblog.core.session import Session


class FlashMessagesMixin(object):

    @property
    def messages(self):
        if not hasattr(self, '_messages'):
            messages = self.get_secure_cookie('flash_messages')
            self._messages = []
            if messages:
                self._messages = tornado.escape.json_decode(messages)
        return self._messages

    def flash(self, message, type='error'):
        self.messages.append((type, message))
        self.set_secure_cookie(
            'flash_messages',
            tornado.escape.json_encode(self.messages)
        )

    def get_flashed_messages(self):
        messages = self.messages
        self._messages = []
        self.clear_cookie('flash_messages')
        return messages


class BaseHandler(RequestHandler, FlashMessagesMixin):

    def render_string(self, template_name, **context):
        context.update({
            'xsrf': self.xsrf_form_html,
            'request': self.request,
            'user': self.current_user,
            'static': self.static_url,
            'handler': self, })

        return self._jinja_render(
            path=self.get_template_path(),
            filename=template_name,
            auto_reload=self.settings['debug'],
            **context)

    def _jinja_render(self, path, filename, **context):
        template = self.application.jinja_env.get_template(
            filename, parent=path)
        self.write(template.render(**context))

    @property
    def is_xhr(self):
        return self.request.headers.get('X-Requested-With', '').lower()\
            == 'xmlhttprequest'

    @property
    def session(self):
        if hasattr(self, '_session'):
            return self._session
        else:
            session_id = self.get_secure_cookie('sid')
            self._session = Session(self.application.session_store, session_id,
                                    expires_days=1)
            if not session_id:
                self.set_secure_cookie('sid', self._session.id, expires_days=1)
            return self._session

    def get_current_user(self):
        return self.session['user'] if 'user' in self.session else None

    def get_object_or_404(self, model, **kwargs):
        try:
            return model.get(**kwargs)
        except model.DoesNotExist:
            raise HTTPError(404)

    @property
    def next_url(self):
        return self.get_argument("next", None)


class AdminBaseHandler(BaseHandler):
    def prepare(self):
        if not self.current_user:
            if self.request.method == "GET":
                url = self.get_login_url()
                if "?" not in url:
                    url += "?" + urllib.urlencode(
                        dict(next=self.request.full_url()))
                self.redirect(url)
            raise HTTPError(403)
        super(AdminBaseHandler, self).prepare()
