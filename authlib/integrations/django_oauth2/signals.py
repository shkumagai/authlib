# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.dispatch import Signal


#: signal when client is authenticated
client_authenticated = Signal()

#: signal when token is revoked
token_revoked = Signal()

#: signal when token is authenticated
token_authenticated = Signal()
