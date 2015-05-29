# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('fcompany', '0004_company_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='user',
            field=models.ForeignKey(related_name='companies', to=settings.AUTH_USER_MODEL),
        ),
    ]
