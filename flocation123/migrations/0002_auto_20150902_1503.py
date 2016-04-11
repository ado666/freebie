# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flocation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=datetime.datetime(2015, 9, 2, 11, 3, 58, 947769, tzinfo=utc), serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='lng',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='uuid',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
