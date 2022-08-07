from django.urls import reverse
import json
from rest_framework.test import APITestCase


class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('login')
        data = '{"username": "admin", "password": "admin"}'
        jsondata = json.loads(data)
        response = self.client.post(url, jsondata)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, data)

