from django.test import TestCase
from django.http import HttpRequest

from tank.models import User, UserProfile

from tank.views import user_login

class TankHomeTests(TestCase):

    def test_user_login(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['username'] = 'a'
        request.POST['password'] = 'a'
        response = user_login(request)
        self.assertIn('Hello', response.context)
        
