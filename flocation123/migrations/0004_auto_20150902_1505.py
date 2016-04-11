# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flocation', '0003_auto_20150902_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='time',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
