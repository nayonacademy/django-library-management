# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbook',
            name='image',
            field=models.FileField(upload_to='files/%Y/%m/%d'),
        ),
    ]
