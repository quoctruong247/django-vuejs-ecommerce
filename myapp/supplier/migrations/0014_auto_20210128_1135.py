# Generated by Django 3.1.5 on 2021-01-28 04:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0013_auto_20210128_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 11, 35, 10, 336401)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 11, 35, 10, 336401)),
        ),
    ]
