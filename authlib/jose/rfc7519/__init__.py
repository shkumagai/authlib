# -*- coding: utf-8 -*-
"""
    authlib.jose.rfc7519
    ~~~~~~~~~~~~~~~~~~~~

    This module represents a direct implementation of
    JSON Web Token (JWT).

    https://tools.ietf.org/html/rfc7519
"""
from __future__ import absolute_import, unicode_literals

from .jwt import JsonWebToken
from .claims import BaseClaims, JWTClaims


__all__ = ['JsonWebToken', 'BaseClaims', 'JWTClaims']
