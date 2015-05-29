# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fcompany', '0003_auto_20150528_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='icon',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
