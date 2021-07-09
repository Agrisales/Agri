from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(models.Product)

class Product_add(ImportExportModelAdmin):
    pass