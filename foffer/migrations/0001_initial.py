# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('fcompany', '__first__'),
        ('faddress', '0002_remove_address_address'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fuser', '0005_user_ignore_notifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=200)),
                ('dist', models.CharField(max_length=5)),
                ('icon', models.CharField(max_length=200)),
                ('date_start', models.DateField(default=None)),
                ('date_end', models.DateField(default=None)),
                ('time_start', models.TimeField(default=None)),
                ('time_end', models.TimeField(default=None)),
                ('mo', models.BooleanField(default=False)),
                ('tu', models.BooleanField(default=False)),
                ('we', models.BooleanField(default=False)),
                ('th', models.BooleanField(default=False)),
                ('fr', models.BooleanField(default=False)),
                ('sa', models.BooleanField(default=False)),
                ('su', models.BooleanField(default=False)),
                ('lat', models.FloatField(default=None)),
                ('lng', models.FloatField(default=None)),
                ('addresses', models.ManyToManyField(related_name='offers', to='faddress.Address')),
            ],
        ),
        migrations.CreateModel(
            name='OfferCategory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OfferToUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_send', models.DateTimeField(default=None)),
                ('offer', models.ForeignKey(to='foffer.Offer')),
                ('user', models.ForeignKey(to='fuser.User')),
            ],
        ),
        migrations.AddField(
            model_name='offer',
            name='category',
            field=models.ForeignKey(related_name='offers', default=1, blank=True, to='foffer.OfferCategory'),
        ),
        migrations.AddField(
            model_name='offer',
            name='company',
            field=models.ForeignKey(related_name='offers', to='fcompany.Company'),
        ),
        migrations.AddField(
            model_name='offer',
            name='user',
            field=models.ForeignKey(related_name='all_offers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='offertouser',
            unique_together=set([('offer', 'user')]),
        ),
    ]
