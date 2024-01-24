from django.db import models
from ..managers import UserManager


class User(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    full_name = models.CharField(max_length=55)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # add UserManager Objects
    objects = UserManager

    # this field should be unique = True
    USERNAME_FIELD = 'phone_number'  # when run: python manage.py createsuperuser this field authentication user.

    REQUIRED_FIELDS = ['email', 'full_name']  # when make superuser this field question

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):  # permission user to admin panel
        return True

    def has_module_perms(self, app_label):  # permission user module
        return True

    @property
    def is_staff(self):  # user is superuser? if is_admin:True ,  User can be is_staff
        return self.is_admin
