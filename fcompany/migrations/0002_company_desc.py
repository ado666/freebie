# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fcompany', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='desc',
            field=models.CharField(default=datetime.datetime(2015, 5, 27, 11, 31, 56, 346182, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
