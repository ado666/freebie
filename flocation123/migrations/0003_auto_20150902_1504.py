# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flocation', '0002_auto_20150902_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='id',
        ),
        migrations.AlterField(
            model_name='location',
            name='uuid',
            field=models.CharField(max_length=200, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
