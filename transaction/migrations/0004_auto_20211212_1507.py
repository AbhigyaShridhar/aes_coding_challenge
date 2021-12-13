# Generated by Django 3.1.13 on 2021-12-12 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_auto_20211212_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactionlineitemdetails',
            name='tn_time',
        ),
        migrations.AddField(
            model_name='transaction',
            name='tn_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='unit',
            field=models.CharField(choices=[('METER', 'METER'), ('KG', 'KG')], default='KG', max_length=5),
        ),
        migrations.AlterField(
            model_name='transactionlineitemdetails',
            name='required_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 12, 15, 7, 42, 417411)),
        ),
        migrations.AlterField(
            model_name='transactionlineitemdetails',
            name='unit',
            field=models.CharField(choices=[('METER', 'METER'), ('KG', 'KG')], default='KG', max_length=5),
        ),
    ]
