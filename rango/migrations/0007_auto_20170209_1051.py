# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-09 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20170209_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=123),
        ),
    ]
