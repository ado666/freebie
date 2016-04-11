# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fuser', '0002_user_last_login'),
        ('flocation', '0011_auto_20150908_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='uuid',
        ),
        migrations.AddField(
            model_name='location',
            name='user',
            field=models.ForeignKey(related_name='all_locations', default=None, to='fuser.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 10, 51, 52, 542479)),
            preserve_default=True,
        ),
    ]
