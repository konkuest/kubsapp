# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-29 14:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0004_student_follow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='follow',
        ),
    ]