# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20171121_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='tag_description',
            field=models.TextField(default=''),
        ),
    ]
