# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('flocation', '0014_auto_20150908_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='uuid',
        ),
        migrations.AlterField(
            model_name='location',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 10, 58, 13, 635515)),
            preserve_default=True,
        ),
    ]
