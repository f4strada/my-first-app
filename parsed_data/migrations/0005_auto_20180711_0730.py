# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-11 07:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0004_auto_20180711_0728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='naverdata',
            old_name='urllink',
            new_name='urlLink',
        ),
    ]