from django.db import models
from django.contrib.auth.models import User as DjangoUser
from fcompany.models import Company
from faddress.models import Address
from django.conf import settings
from fuser.models import User
import json

# Create your models here.
class OfferCategory(models.Model):
     id = models.AutoField(primary_key=True)
     name = models.CharField(max_length=200)

class Offer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)

    dist = models.CharField(max_length=5)
    icon = models.CharField(max_length=200)

    date_start  = models.DateField(default=None)
    date_end    = models.DateField(default=None)
    time_start  = models.TimeField(default=None)
    time_end    = models.TimeField(default=None)

    mo          = models.BooleanField(default=False)
    tu          = models.BooleanField(default=False)
    we          = models.BooleanField(default=False)
    th          = models.BooleanField(default=False)
    fr          = models.BooleanField(default=False)
    sa          = models.BooleanField(default=False)
    su          = models.BooleanField(default=False)

    lat         = models.FloatField(default=None)
    lng         = models.FloatField(default=None)

    category    = models.ForeignKey(OfferCategory, related_name="offers")

    is_my       = False

    user = models.ForeignKey(DjangoUser, related_name="all_offers")
    company = models.ForeignKey(Company, related_name="offers")

    addresses = models.ManyToManyField(Address, related_name="offers")

    def json(self):
        aa  = hasattr(self, "all_addresses")
        if not aa:
            aa = []
        else:
            aa = [a.json() for a in self.all_addresses.all()]

        return {
            'id': self.id,
            'name': self.name,
            'desc': self.desc,
            'dist': self.dist,
            'icon': self.icon,

            # 'sdate': self.date_start.strftime("%A, %d. %B %Y %I:%M%p"),
            'sdate': self.date_start.strftime("%d-%m-%Y"),
            'edate': self.date_end.strftime("%d-%m-%Y"),
            # 'edate': self.date_end,
            'stime': self.time_start.strftime("%H-%M"),
            'etime': self.time_end.strftime("%H-%M"),

            'mo'   : self.mo,
            'tu'   : self.tu,
            'we'   : self.we,
            'th'   : self.th,
            'fr'   : self.fr,
            'sa'   : self.sa,
            'su'   : self.su,

            'category': self.category,

            'lat'  : self.lat,
            'lng'  : self.lng,

            'is_my': self.is_my,
            'all_addresses': aa,
            'addresses': [a.json() for a in self.addresses.all()],
        }


class OfferToUser(models.Model):

    offer = models.ForeignKey(Offer)
    user = models.ForeignKey(User)
    last_send  = models.DateTimeField(default=None)

    class Meta:
        unique_together = (("offer", "user"),)

