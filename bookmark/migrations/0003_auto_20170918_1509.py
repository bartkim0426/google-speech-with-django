# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0002_bookmark_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='hover',
            field=models.CharField(blank=True, help_text='홈페이지에서 해당 링크에 마우스를 올렸을 때 나오는 도움말입니다. 아이디/비밀번호 등 원하는 정보를 적어주세요.', max_length=255, null=True, verbose_name='도움말'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='icon',
            field=models.CharField(default='explore', help_text='material icon 이름(https://material.io/icons/ 참고)을 입력해주세요 ex)face', max_length=20, verbose_name='아이콘이름'),
        ),
    ]
