# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0003_auto_20170918_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='order',
            field=models.IntegerField(blank=True, null=True, verbose_name='순번'),
        ),
    ]