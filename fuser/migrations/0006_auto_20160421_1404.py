# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fcompany', '__first__'),
        ('fuser', '0005_user_ignore_notifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFavorites',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.ForeignKey(to='fcompany.Company')),
                ('user', models.ForeignKey(to='fuser.User')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='userfavorites',
            unique_together=set([('company', 'user')]),
        ),
    ]
