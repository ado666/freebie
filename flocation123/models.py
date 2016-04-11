from django.db import models

# Create your models here.

class Location(models.Model):
    #id = models.AutoField(primary_key=True)
    #uuid = models.CharField(max_length=200)
    #lng = models.FloatField()
    #lat = models.FloatField()
#    time = models.DateTimeField()

    def json(self):
        return {
            'uuid': self.uuid,
            'lng': self.lng,
            'lat': self.lat,
            #'time': self.time,
        }
