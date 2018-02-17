# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-17 05:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('number', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('day', models.CharField(blank=True, max_length=20)),
                ('image', models.CharField(blank=True, max_length=300, null=True)),
                ('content', models.TextField(max_length=500)),
                ('author', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('studentid', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('follow', models.CharField(max_length=100)),
                ('represent', models.CharField(default=99, max_length=200)),
            ],
        ),
    ]