# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('flocation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 15, 36, 10, 277621)),
            preserve_default=True,
        ),
    ]
