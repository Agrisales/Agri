from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields import EmailField


class UserManager(BaseUserManager):
    def create_user(self, user_name, email, phone_number, password=None):
        user = self.model(
            user_name=user_name,
            phone_number=phone_number,
            email=email
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, email, phone_number, password):
        user = self.create_user(
            user_name=user_name,
            password=password,
            phone_number=phone_number,
            email=email
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    phone_number = models.TextField(
        verbose_name="Phone number", max_length=10, unique=True, primary_key=True)
    user_name = models.CharField(verbose_name="User name", max_length=64)
    date_joined = models.DateTimeField(
        verbose_name="Date joined", auto_now_add=True)
    last_login = models.DateTimeField(
        verbose_name="Last login", auto_now_add=True)
    email = EmailField(verbose_name="email")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["user_name", "password", "email"]

    object = UserManager()

    def __str__(self):
        return f"{self.phone_number}     {self.user_name}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
