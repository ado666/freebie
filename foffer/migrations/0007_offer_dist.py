# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foffer', '0006_auto_20150615_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='dist',
            field=models.CharField(default='100', max_length=5),
            preserve_default=False,
        ),
    ]
