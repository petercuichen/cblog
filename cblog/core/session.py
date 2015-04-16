#!/usr/bin/env python2
# coding=utf8

from __future__ import absolute_import, division, print_function

import cPickle as pickle
from uuid import uuid4
import time
import logging

from .db import DBSession


class RedisSessionStore(object):

    default_expire = 7 * 24 * 3600
    default_prefix = 'session'

    def __init__(self, redis_connection):
        self.redis = redis_connection

    def prefixed(self, sid):
        return '%s:%s' % (self.default_prefix, sid)

    def generate_sid(self):
        return uuid4().get_hex()

    def get_session(self, sid, name):
        data = self.redis.hget(self.prefixed(sid), name)
        session = pickle.loads(data) if data else dict()
        return session

    def set_session(self, sid, session_data, name, expiry=default_expire):
        self.redis.hset(self.prefixed(sid), name, pickle.dumps(session_data))
        if expiry:
            self.redis.expire(self.prefixed(sid), expiry)

    def delete_session(self, sid):
        self.redis.delete(self.prefixed(sid))


class Session(object):
    def __init__(self, session_cache, session_id=None, expires_days=None):
        self._cache = session_cache
        self._db = DBSession
        self._sid = session_id if session_id else self._cache.generate_sid()
        self._dirty = False
        self.set_expires(expires_days)
        try:
            self._data = self._cache.get_session(self._sid, 'data')
        except:
            logging.error('Can not connect Redis server.')
            self._data = {}

    def clear(self):
        self._cache.delete_session(self._sid)

    @property
    def id(self):
        return self._sid

    def access(self, remote_ip):
        access_info = {'remote_ip': remote_ip, 'time': '%.6f' % time.time()}
        self._cache.set_session(
            self._sid,
            'last_access',
            pickle.dumps(access_info))

    def last_access(self):
        access_info = self._cache.get_session(self._sid, 'last_access')
        return pickle.loads(access_info)

    def set_expires(self, days):
        self._expiry = days * 86400 if days else None

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value
        self._dirty = True

    def __delitem__(self, key):
        del self._data[key]
        self._dirty = True

    def __len__(self):
        return len(self._data)

    def __contains__(self, key):
        return key in self._data

    def __iter__(self):
        for key in self._data:
            yield key

    def __repr__(self):
        return self._data.__repr__()

    def __del__(self):
        self.save()

    def save(self):
        if self._dirty:
            self._cache.set_session(self._sid, self._data, 'data', self._expiry)
            self._dirty = False