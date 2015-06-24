from django.db import models
from django.contrib.auth.models import User
from fcompany.models import Company

# Create your models here.

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

    user = models.ForeignKey(User, related_name="all_offers")
    company = models.ForeignKey(Company, related_name="offers")

    def json(self):
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

            'lat'  : self.lat,
            'lng'  : self.lng
        }