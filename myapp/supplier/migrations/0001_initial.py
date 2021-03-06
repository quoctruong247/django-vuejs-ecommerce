# Generated by Django 3.1.1 on 2021-01-21 04:41

import datetime
from django.db import migrations, models
import supplier.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=supplier.models.upload_image_path_supplier)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=supplier.models.upload_image_path_supplier)),
                ('ordering', models.IntegerField(default=1)),
                ('available', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 1, 21, 11, 41, 2, 528301))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2021, 1, 21, 11, 41, 2, 528301))),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
