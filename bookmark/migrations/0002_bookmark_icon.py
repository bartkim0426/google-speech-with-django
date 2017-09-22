# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='icon',
            field=models.CharField(default='explore', help_text='material icon 이름(https://material.io/icons/)을 입력해주세요 ex)face', max_length=20, verbose_name='아이콘이름'),
        ),
    ]