# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('uuid', models.AutoField(serialize=False, primary_key=True)),
                ('lng', models.FloatField(max_length=200)),
                ('lat', models.FloatField(max_length=200)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
