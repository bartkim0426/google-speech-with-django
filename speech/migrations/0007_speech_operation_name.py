# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speech', '0006_auto_20170911_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='speech',
            name='operation_name',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
