# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-22 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0004_auto_20190322_2041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='neighbourhood',
            new_name='neighbourhood_id',
        ),
        migrations.AddField(
            model_name='business',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
