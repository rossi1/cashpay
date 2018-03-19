import unittest
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse_lazy
from ..utils import request_url

class LoginTestCase(APITestCase):

    def setUp(self):
        self.token_url = reverse_lazy('request-token')
        self.factory = APIClient()
        self.login_url = reverse_lazy('login')
        self.param = {"usr":"emma rossi", "pwd":"my name is emma rossi",
        "device_data": "opera"}

    def test_login_view(self):
        response = self.factory.post(self.login_url, self.param, format='json')

        self.assertTrue(response.status_code == 200)
        print(response.body)
        #self.assertTrue(response.reason, )


if __name__ == '__main__':
    unittest.main()