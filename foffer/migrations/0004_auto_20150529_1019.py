# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foffer', '0003_auto_20150529_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='date_end',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='offer',
            name='date_start',
            field=models.DateField(default=None),
        ),
    ]
