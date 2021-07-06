from django.db import models


class Product_seed(models.Model):
    name = models.CharField(verbose_name="Seed name",primary_key=True,max_length=255)
    imagelink = models.URLField(verbose_name="Image link")
    price = models.IntegerField(verbose_name="Price")
    description = models.TextField(verbose_name="Description")
    