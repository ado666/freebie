# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fcompany', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('lat', models.FloatField(default=None)),
                ('lng', models.FloatField(default=None)),
                ('address', models.CharField(max_length=200)),
                ('company', models.ForeignKey(related_name='addresses', to='fcompany.Company')),
            ],
        ),
    ]
