#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

from . import BaseHandler
from cblog.app.web import user as user_base
from cblog.core.exc import LoginExc


class LoginHandler(BaseHandler):
    def get(self):
        is_login = self.current_user
        if not is_login:
            self.render('admin/login.html')

        # TODO tmp here
        self.redirect('/admin')

    def post(self):
        name = self.get_argument('username', None)
        pwd = self.get_argument('password', None)
        try:
            if not name or not pwd:
                raise LoginExc(u'请输入用户名或密码')

            user = user_base.get(name)
            if not user or not user_base.check_pwd(user):
                raise LoginExc(u'用户名密码错误，请重新输入')

            self.session['user'] = user
            self.session.save()
            self.redirect('/admin')
            return
        except LoginExc as e:
            self.flash(e.msg)

        self.render('admin/login.html')
        return


class LogoutHandler(BaseHandler):
    def get(self):
        del self.session["user"]
        self.session.save()
        self.redirect(self.get_login_url())
        return

