from django.db import models

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10, primary_key=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
