# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 22:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sala', '0002_auto_20161112_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wydarzenie',
            name='date',
        ),
        migrations.AddField(
            model_name='wydarzenie',
            name='podajdate',
            field=models.DateField(default=datetime.date(2016, 1, 1)),
        ),
    ]
