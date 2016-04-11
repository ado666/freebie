# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('flocation', '0024_auto_20150910_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 12, 34, 36, 392889)),
            preserve_default=True,
        ),
    ]
