from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User
from accounts.forms import UserRegistrationForm, UserLoginForm, VerifyCodeForm


class TestUserRegistrationView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_register_GET(self):
        response = self.client.get(reverse('accounts:user_register'))
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response , 'accounts/register.html')
        self.failUnless(response.context['form'] , UserRegistrationForm)

    def test_user_register_POST_valid(self):
        response = self.client.post(reverse('accounts:user_register'),data={
            'phone_number':'09131111111',
            'email' : 'test-1@email.com',
            'full_name': 'test-1',
            'password':'test',
        })
        self.assertEqual(response.status_code , 302)
        self.assertRedirects(response , reverse('accounts:verify_code'))

