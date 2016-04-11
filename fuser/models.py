from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=200)
    token = models.CharField(max_length=200)

    last_login = models.DateTimeField(default=None)
    last_send = models.DateTimeField(default=None)

    current_lng = models.FloatField(default=None)
    current_lat = models.FloatField(default=None)

    ignore_notifications = models.BooleanField(default=False)

    def json(self):
        return {
            'id': self.id,
            'uuid': self.uuid,
            'token': self.token,
        }
