# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-24 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher_name', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=30)),
            ],
        ),
        migrations.RenameModel(
            old_name='Post',
            new_name='Comic',
        ),
    ]