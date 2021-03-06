# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-23 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0008_auto_20190323_0942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorities',
            name='authority_email',
        ),
        migrations.RemoveField(
            model_name='news',
            name='notification',
        ),
        migrations.AddField(
            model_name='news',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='healthservices',
            name='healthservices',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
