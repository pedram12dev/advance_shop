from django.test import SimpleTestCase
from django.urls import reverse , resolve
from accounts.views import UserRegisterView , UserLoginView , UserLogoutView , UserVerifyCodeView


class TestUrls(SimpleTestCase):
    def test_user_register_url(self):
        url = reverse('accounts:user_register')
        self.assertEqual(resolve(url).func.view_class , UserRegisterView)

    def test_user_login_url(self):
        url = reverse('accounts:user_login')
        self.assertEqual(resolve(url).func.view_class , UserLoginView)

    def test_user_logout_url(self):
        url = reverse('accounts:user_logout')
        self.assertEqual(resolve(url).func.view_class , UserLogoutView)

    def test_user_verify_code_url(self):
        url = reverse('accounts:verify_code')
        self.assertEqual(resolve(url).func.view_class , UserVerifyCodeView)