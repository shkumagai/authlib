# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from .okp_key import OKPKey
from .jws_eddsa import register_jws_rfc8037


__all__ = ['register_jws_rfc8037', 'OKPKey']
