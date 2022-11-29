from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from userapp.managers import CustomUserManager


class CustomAdminUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=128, unique=True)
    custom_password = models.CharField(max_length=10, null=False, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if not self.is_superuser:
            self.set_password(self.custom_password)
        super(CustomAdminUser, self).save(*args, **kwargs)
