# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-22 17:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0003_auto_20190322_2015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='neighbourhood_id',
            new_name='neighbourhood',
        ),
    ]
