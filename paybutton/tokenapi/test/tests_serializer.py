import unittest
from django.test import TestCase
from ..serializer import SerializerUser, SerializerToken
from ..jt import Jwt


class SerializerTestCase(TestCase):

    def setUp(self):
        self.detail = {"usr": "emma", "pwd": "complex"}

        jwt = Jwt()

        self.url = {'token': jwt.encode_token('user').decode(),
                    'url': 'https://facebook.com'}

    def test_user(self):

        serial = SerializerUser(data=self.detail)

        self.assertTrue(serial.is_valid(raise_exception=True))

    def test_url(self):
        serial = SerializerToken(data=self.url)

        self.assertTrue(serial.is_valid(raise_exception=True))


if __name__ == '__main__':
    unittest.main()