# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-16 09:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0010_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='first_visit',
        ),
        migrations.RemoveField(
            model_name='page',
            name='last_visit',
        ),
    ]
