# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-23 06:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0007_auto_20190322_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='health',
            name='health_email',
        ),
        migrations.RemoveField(
            model_name='health',
            name='healthservices',
        ),
    ]
