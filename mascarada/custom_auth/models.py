from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager

class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=255,unique=True)
    
    is_active = models.BinaryField(default=True)
    is_admin = models.BinaryField(default=False)
    is_superuser = models.BinaryField(default=False)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    
    REQUIRED_FIELDS = ['emial']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin