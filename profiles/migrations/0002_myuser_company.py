# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-16 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='company',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]