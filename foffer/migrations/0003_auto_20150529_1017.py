# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('foffer', '0002_auto_20150529_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='date_end',
            field=models.DateField(default=datetime.datetime(2015, 5, 29, 10, 17, 14, 746583)),
        ),
        migrations.AlterField(
            model_name='offer',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2015, 5, 29, 10, 17, 14, 746547)),
        ),
    ]
