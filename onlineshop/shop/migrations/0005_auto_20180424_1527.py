# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-24 14:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20180424_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comic',
            name='publisher',
        ),
        migrations.DeleteModel(
            name='Comic',
        ),
    ]