from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import LoginForm, SignupForm

class CoreAppTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.login_url = reverse('core:login')
        self.signup_url = reverse('core:signup')

    def test_login_view(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/login.html')
        self.assertIsInstance(response.context['form'], LoginForm)

        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 302)  

        data = {'username': 'invaliduser', 'password': 'invalidpassword'}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 200)  