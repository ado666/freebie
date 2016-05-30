# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuser', '0006_auto_20160421_1404'),
        ('foffer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryToUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.ForeignKey(to='foffer.OfferCategory')),
                ('user', models.ForeignKey(to='fuser.User')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='categorytouser',
            unique_together=set([('user', 'category')]),
        ),
    ]
