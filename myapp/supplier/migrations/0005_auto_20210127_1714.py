# Generated by Django 3.1.5 on 2021-01-27 10:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0004_auto_20210127_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 27, 17, 14, 42, 681343)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 27, 17, 14, 42, 681343)),
        ),
    ]
