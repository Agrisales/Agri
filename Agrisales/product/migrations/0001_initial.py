# Generated by Django 3.2.4 on 2021-07-06 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_seed',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Seed name')),
                ('imagelink', models.URLField(verbose_name='Image link')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('category', models.TextField(verbose_name='category')),
            ],
        ),
    ]
