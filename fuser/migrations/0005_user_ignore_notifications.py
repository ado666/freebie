# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuser', '0004_user_last_send'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ignore_notifications',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
