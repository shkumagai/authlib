import os
from authlib.integrations.django_oauth1 import (
    CacheAuthorizationServer,
)
from tests.django_helper import TestCase as _TestCase
from .models import Client, TokenCredential


class TestCase(_TestCase):
    def setUp(self):
        super(TestCase, self).setUp()
        os.environ['AUTHLIB_INSECURE_TRANSPORT'] = 'true'

    def tearDown(self):
        os.environ.pop('AUTHLIB_INSECURE_TRANSPORT')
        super(TestCase, self).tearDown()

    def create_server(self):
        return CacheAuthorizationServer(Client, TokenCredential)
