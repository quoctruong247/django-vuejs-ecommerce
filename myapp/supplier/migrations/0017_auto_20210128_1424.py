# Generated by Django 3.1.5 on 2021-01-28 07:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0016_auto_20210128_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 14, 23, 57, 235618)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 14, 23, 57, 235618)),
        ),
    ]
