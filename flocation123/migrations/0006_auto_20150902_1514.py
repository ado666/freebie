# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flocation', '0005_auto_20150902_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='location',
            name='lng',
        ),
        migrations.RemoveField(
            model_name='location',
            name='uuid',
        ),
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
            preserve_default=True,
        ),
    ]
