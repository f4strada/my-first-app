# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-11 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0003_auto_20180711_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='naverdata',
            name='urllink',
            field=models.URLField(),
        ),
    ]
