# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-11 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NaverData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('imgLink', models.URLField()),
                ('urllink', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='BlogData',
        ),
    ]
