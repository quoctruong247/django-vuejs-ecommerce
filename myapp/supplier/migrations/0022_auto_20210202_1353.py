# Generated by Django 3.1.6 on 2021-02-02 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0021_auto_20210202_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 2, 13, 53, 13, 507875)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 2, 13, 53, 13, 507875)),
        ),
    ]
