# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foffer', '0005_auto_20150615_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='lat',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='offer',
            name='lng',
            field=models.FloatField(default=None),
        ),
    ]
