# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 02:13
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0005_auto_20171121_0827'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='bookinfo',
            managers=[
                ('books1', django.db.models.manager.Manager()),
            ],
        ),
    ]
