# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-06-08 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksystem', '0002_auto_20190607_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='is_favourite',
            field=models.BooleanField(default=False),
        ),
    ]