# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 02:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speech', '0015_auto_20170915_1629'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WeatherLocation',
        ),
    ]
