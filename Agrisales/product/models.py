from django.db import models


class Product(models.Model):
    id = models.CharField(verbose_name="Product name",primary_key=True,max_length=255)
    imagelink = models.TextField(verbose_name="Image link")
    price = models.TextField(verbose_name="Price")
    description = models.TextField(verbose_name="Description")
    category = models.TextField(verbose_name="category",max_length= 255)
    rating = models.IntegerField(verbose_name="Ratings")
    

    def __str__(self):
        return self.id


class Order(models.Model):
    product_name = models.TextField(verbose_name="Product Name",max_length=255)
    quantity = models.IntegerField(verbose_name="Quantity")
    price = models.IntegerField(verbose_name="price")
    user = models.TextField(verbose_name="User")
    