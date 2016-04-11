# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('flocation', '0012_auto_20150908_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='uuid',
            field=models.CharField(default=None, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 10, 53, 18, 959094)),
            preserve_default=True,
        ),
    ]
