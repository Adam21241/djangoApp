# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 21:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wydarzenie',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='wydarzenie',
            name='kto',
            field=models.CharField(default='', max_length=20),
        ),
    ]