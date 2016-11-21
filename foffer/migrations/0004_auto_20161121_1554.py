# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foffer', '0003_categorytouser_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='desc',
            field=models.CharField(max_length=1024),
        ),
    ]
