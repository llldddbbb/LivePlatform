# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 17:10
from __future__ import unicode_literals

import backend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20170803_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liveroom',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='liveroom',
            name='slide_path',
            field=models.FileField(default='default', upload_to=backend.models.get_file_path),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.FileField(default='default.jpg', upload_to='avatar/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date joined'),
        ),
    ]
