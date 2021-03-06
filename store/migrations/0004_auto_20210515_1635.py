# Generated by Django 2.2.19 on 2021-05-15 16:35

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='p_name',
            field=models.CharField(choices=[(11, 'Hand Sanitizer'), (2, 'Surgical mask - Box (50 pcs)'), (101, 'Hair Growth and Nourishment Combo'), (19, 'Hairfall Control Combo'), (10, 'Clear Shampoo Men Cool Sport Menthol Anti Dandruff 180ml'), (22, 'Test01'), (20, '2')], default='select', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.IntegerField(default=store.models.unique_order_id, unique=True),
        ),
    ]
