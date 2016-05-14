# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 17:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=45)),
                ('author_name', models.CharField(max_length=45)),
                ('unique_no', models.CharField(blank=True, max_length=45, null=True, unique=True)),
                ('description', models.TextField()),
                ('image', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='AddStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('father_name', models.CharField(max_length=45)),
                ('mother_name', models.CharField(max_length=45)),
                ('unique_id', models.CharField(blank=True, max_length=45, null=True, unique=True)),
                ('phone', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='LogFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_book', models.IntegerField()),
                ('borrow', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.AddBook')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.AddStudent')),
            ],
        ),
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.AddStudent')),
            ],
        ),
        migrations.AddField(
            model_name='addbook',
            name='category_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Category'),
        ),
    ]
