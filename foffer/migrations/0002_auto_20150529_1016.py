# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('foffer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='date_end',
            field=models.DateField(default=datetime.datetime(2015, 5, 29, 10, 16, 26, 419295)),
        ),
        migrations.AddField(
            model_name='offer',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2015, 5, 29, 10, 16, 26, 419235)),
        ),
        migrations.AddField(
            model_name='offer',
            name='days',
            field=models.BinaryField(default=b'0b0'),
        ),
        migrations.AddField(
            model_name='offer',
            name='time_end',
            field=models.TimeField(default=None),
        ),
        migrations.AddField(
            model_name='offer',
            name='time_start',
            field=models.TimeField(default=None),
        ),
    ]
