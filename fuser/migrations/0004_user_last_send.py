# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuser', '0003_auto_20150908_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_send',
            field=models.DateTimeField(default=None),
            preserve_default=True,
        ),
    ]
