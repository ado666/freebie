from django.db import models
from datetime import datetime
from fuser.models import User
# Create your models here.

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    # uuid = models.CharField(max_length=200, default=None)
    lng = models.FloatField()
    lat = models.FloatField()
    time = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, related_name="all_locations", default=None)

    def json(self):
        return {
            'uuid': self.uuid,
            'lng': self.lng,
            'lat': self.lat,
            #'time': self.time,
        }
