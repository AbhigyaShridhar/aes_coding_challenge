# Generated by Django 3.1.13 on 2021-12-13 03:54

import datetime
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0008_auto_20211213_0850'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='transaction',
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='unit',
            field=models.CharField(choices=[('KG', 'KG'), ('METER', 'METER')], default='KG', max_length=5),
        ),
        migrations.AlterField(
            model_name='transactionlineitemdetails',
            name='required_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 13, 9, 24, 26, 165226)),
        ),
        migrations.AlterField(
            model_name='transactionlineitemdetails',
            name='unit',
            field=models.CharField(choices=[('KG', 'KG'), ('METER', 'METER')], default='KG', max_length=5),
        ),
    ]
