# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speech', '0013_weatherlocation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weatherlocation',
            options={'ordering': ['order'], 'verbose_name': '날씨 위치', 'verbose_name_plural': '날씨 위치 관리'},
        ),
        migrations.AddField(
            model_name='weatherlocation',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='활성화'),
        ),
        migrations.AddField(
            model_name='weatherlocation',
            name='order',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='순번'),
        ),
    ]