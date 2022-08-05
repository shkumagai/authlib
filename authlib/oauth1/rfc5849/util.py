# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from authlib.common.urls import quote, unquote


def escape(s):
    return quote(s, safe=b'~')


def unescape(s):
    return unquote(s)
