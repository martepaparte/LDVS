from django.test import TestCase
from django.test import Client



class LoginTesting(TestCase):
    def test_doLogin(self):
        response = Client().post('/login/', {'username': 'lala@lala.com', 'password': 'admin'})
        self.assertEqual(response.status_code, 200)
