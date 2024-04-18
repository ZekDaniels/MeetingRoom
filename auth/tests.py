from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.conf import settings

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.endpoint = settings.BACKEND_URL + "auth/login/"

    def test_login_success(self):
        response = self.client.post(self.endpoint, {
            'username': 'testuser',
            'password': 'testpassword'
        })

        self.assertEqual(response.status_code, 200)
        # Token'ı al
        token = Token.objects.get(user__username='testuser')
        #User Token'ı kontrol et
        user = User.objects.get(username='testuser')
        self.assertEqual(token.key, user.auth_token.key)
        # Token'ı sakla
        self.client.defaults['HTTP_AUTHORIZATION'] = 'Token ' + token.key
        

    def test_login_failure(self):
        response = self.client.post(self.endpoint, {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 400)
# Şimdi, Token'ı sakladık. Diğer testlerde bu token'ı kullanabiliriz.
