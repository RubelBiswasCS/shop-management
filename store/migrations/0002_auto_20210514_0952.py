# Generated by Django 2.2.19 on 2021-05-14 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.IntegerField(unique=True),
        ),
    ]