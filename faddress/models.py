from django.db import models
from django.contrib.auth.models import User
from fcompany.models import Company
from django.conf import settings

# Create your models here.
class Address(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    lat         = models.FloatField(default=None)
    lng         = models.FloatField(default=None)

    is_my       = False

    company = models.ForeignKey(Company, related_name="addresses")

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "lat": self.lat,
            "lng": self.lng,
        }