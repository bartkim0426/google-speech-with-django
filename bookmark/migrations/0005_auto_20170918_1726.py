# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0004_auto_20170918_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='is_active',
            field=models.BooleanField(default=True, help_text='체크를 해제하면 화면에 나타나지 않습니다.', verbose_name='활성화'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='order',
            field=models.IntegerField(blank=True, help_text='순번대로 위에서부터 배치됩니다. 중복되면 먼저 만들어진 순서대로, 적지 않으면 가장 마지막에 나옵니다.', null=True, verbose_name='순번'),
        ),
    ]