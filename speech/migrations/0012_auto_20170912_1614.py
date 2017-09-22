# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speech', '0011_auto_20170912_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speech',
            name='done',
        ),
        migrations.AddField(
            model_name='speech',
            name='convert_done',
            field=models.BooleanField(default=False, verbose_name='변환완료'),
        ),
        migrations.AddField(
            model_name='speech',
            name='transcribe_done',
            field=models.BooleanField(default=False, verbose_name='수정완료'),
        ),
    ]