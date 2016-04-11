# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flocation', '0004_auto_20150902_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='time',
        ),
        migrations.AddField(
            model_name='location',
            name='id',
            field=models.AutoField(default=2, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='uuid',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
