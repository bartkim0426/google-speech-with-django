# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0006_nowdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nowdata',
            name='now',
            field=models.DateTimeField(),
        ),
    ]
