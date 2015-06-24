# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foffer', '0004_auto_20150529_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='days',
        ),
        migrations.AddField(
            model_name='offer',
            name='fr',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='offer',
            name='lat',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='offer',
            name='lng',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='offer',
            name='mo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='offer',
            name='sa',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='offer',
            name='su',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='offer',
            name='th',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='offer',
            name='tu',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='offer',
            name='we',
            field=models.BooleanField(default=False),
        ),
    ]
