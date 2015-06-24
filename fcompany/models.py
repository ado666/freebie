from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name="companies")

    icon = models.CharField(max_length=200)

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'desc': self.desc,
            'icon': self.icon,
            'offers': [o.json() for o in self.offers.all()],
        }
