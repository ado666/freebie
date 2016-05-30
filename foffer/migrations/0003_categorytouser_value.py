# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foffer', '0002_auto_20160523_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorytouser',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]
