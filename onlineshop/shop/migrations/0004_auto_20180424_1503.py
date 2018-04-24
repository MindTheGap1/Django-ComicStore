# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-24 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20180424_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='publisher_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
