# Generated by Django 3.1.5 on 2021-01-28 02:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0005_auto_20210127_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 9, 42, 31, 826681)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 9, 42, 31, 826681)),
        ),
    ]
