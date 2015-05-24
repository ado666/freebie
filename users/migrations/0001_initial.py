# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('companies_created', models.IntegerField(default=0)),
                ('offers_created', models.IntegerField(default=0)),
                ('notifications_sended', models.IntegerField(default=0)),
                ('notifications_readed', models.IntegerField(default=0)),
            ],
        ),
    ]
