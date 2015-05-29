from django.db import models
from django.contrib.auth.models import User
from fcompany.models import Company

# Create your models here.

class Offer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)

    date_start  = models.DateField(default=None)
    date_end    = models.DateField(default=None)
    time_start  = models.TimeField(default=None)
    time_end    = models.TimeField(default=None)
    days        = models.BinaryField(default=bin(0000000))

    lon         = models.IntegerField(default=None)
    alt         = models.IntegerField(default=None)

    user = models.ForeignKey(User, related_name="all_offers")
    company = models.ForeignKey(Company, related_name="offers")