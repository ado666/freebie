# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('uuid', models.CharField(max_length=200)),
                ('token', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
