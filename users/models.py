from django.db import models

# Create your models here.

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    companies_created = models.IntegerField(default=0)
    offers_created = models.IntegerField(default=0)

    notifications_sended = models.IntegerField(default=0)
    notifications_readed = models.IntegerField(default=0)