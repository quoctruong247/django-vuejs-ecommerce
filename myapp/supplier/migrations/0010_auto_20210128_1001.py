# Generated by Django 3.1.5 on 2021-01-28 03:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0009_auto_20210128_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 10, 1, 30, 628395)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 10, 1, 30, 628395)),
        ),
    ]
