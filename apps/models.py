from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, Group as RoleModel, PermissionsMixin
from django.db import models
from django.utils import timezone

from common.models import TSFieldsIndexed


class Role(RoleModel):
    class Meta:
        proxy = True


class UserPermissionsMixin(PermissionsMixin):
    groups = None  # remove this field from super class
    user_permissions = None  # remove this field from super class

    role = models.ForeignKey(Role, null=True, on_delete=models.PROTECT)

    class Meta:
        abstract = True


class SimpleUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.is_active = False
        user.is_staff = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=50, default='')
    company = models.CharField(max_length=50, default='')
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_vendor = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    password = models.CharField(max_length=20, default=None)
    image = models.URLField(blank=True,
                            default='https://hueys-list.s3-ap-southeast-2.amazonaws.com/ScBKUMNEguunnamed.png')
    device_id = models.TextField(default='')
    fb_id = models.TextField(default='')
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name


class Holiday(TSFieldsIndexed):
    day = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=128, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
