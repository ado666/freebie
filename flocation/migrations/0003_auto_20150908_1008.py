# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('flocation', '0002_location_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 10, 8, 52, 952856)),
            preserve_default=True,
        ),
    ]
