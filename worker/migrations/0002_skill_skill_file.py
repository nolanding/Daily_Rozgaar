# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-28 09:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='skill_file',
            field=models.FileField(default=django.utils.timezone.now, upload_to=b''),
            preserve_default=False,
        ),
    ]
