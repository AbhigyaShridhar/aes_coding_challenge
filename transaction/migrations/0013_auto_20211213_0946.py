# Generated by Django 3.1.13 on 2021-12-13 04:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0012_auto_20211213_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='unit',
            field=models.CharField(choices=[('KG', 'KG'), ('METER', 'METER')], default='KG', max_length=5),
        ),
        migrations.AlterField(
            model_name='transactionlineitemdetails',
            name='required_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 13, 9, 46, 54, 253256)),
        ),
        migrations.AlterField(
            model_name='transactionlineitemdetails',
            name='unit',
            field=models.CharField(choices=[('KG', 'KG'), ('METER', 'METER')], default='KG', max_length=5),
        ),
    ]