import unittest
import time
from datetime import timedelta
import jwt
from django.test import TestCase
from ..jt import Jwt


class TokenTestCase(TestCase):

    def setUp(self):
        self.token = Jwt()
        self.param = 'user'

    def test_token(self):
        encode = self.token.encode_token(self.param,
                                         time_phrase=timedelta(seconds=5))

        self.assertIsInstance(encode, bytes)

    def test_decode_method(self):

        decode = self.token.decode_token(b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTExMzYyNDMsInN1YiI6InVzZXIiLCJpYXQiOjE1MjA4OTYyNDN9.Kc9tTmurbpluiB8645OKNyeLeF7NKsGM2nAxOg0MOBw')

        self.assertIsInstance(decode, dict)
        self.assertTrue(decode['sub'], str)


class ValidityTestCase(TokenTestCase):

    def test_valid(self):
        encode = self.token.encode_token('user')

        time.sleep(6)

        try:
            decode = self.token.decode_token(encode)
        except jwt.ExpiredSignatureError:
            mst = 'Signature has expired'
            self.assertTrue(mst)
        else:
            self.assertTrue('is valid')


if __name__ == '__main__':
    unittest.main()
