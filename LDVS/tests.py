from django.test import TestCase
from django.test import Client
from home.models import MyUser
from django.test.utils import override_settings
from LDVS import settings

#
# @override_settings(ROOT_URLCONF='LDVS.urls')

class LoginTesting(TestCase):
    def test_doLogin(self):

        user = MyUser.objects.create_user(email = "lala@lala.com", password = "admin")
        response = Client().post('/login', {'username': 'lala@lala.com', 'password': 'admin'})
        self.assertEqual(response.status_code, 302)
