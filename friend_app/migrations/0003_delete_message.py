# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-20 11:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friend_app', '0002_auto_20180519_2149'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
