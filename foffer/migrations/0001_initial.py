# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fcompany', '0005_auto_20150529_0102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=200)),
                ('icon', models.CharField(max_length=200)),
                ('company', models.ForeignKey(related_name='offers', to='fcompany.Company')),
                ('user', models.ForeignKey(related_name='all_offers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
