# -*- coding: utf-8 -*-
"""
    authlib.oauth2.rfc7592
    ~~~~~~~~~~~~~~~~~~~~~~

    This module represents a direct implementation of
    OAuth 2.0 Dynamic Client Registration Management Protocol.

    https://tools.ietf.org/html/rfc7592
"""
from __future__ import absolute_import, unicode_literals

from .endpoint import ClientConfigurationEndpoint

__all__ = ['ClientConfigurationEndpoint']
