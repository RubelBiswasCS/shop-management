# Generated by Django 2.2.19 on 2021-05-05 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('unit_price', models.FloatField()),
                ('current_stock', models.IntegerField()),
            ],
        ),
    ]
