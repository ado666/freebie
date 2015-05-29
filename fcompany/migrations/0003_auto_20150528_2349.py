# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fcompany', '0002_company_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='icon',
        ),
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
