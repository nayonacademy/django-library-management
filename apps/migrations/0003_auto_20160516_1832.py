# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20160515_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbook',
            name='image',
            field=models.FileField(upload_to='media/%Y/%m/%d'),
        ),
    ]
