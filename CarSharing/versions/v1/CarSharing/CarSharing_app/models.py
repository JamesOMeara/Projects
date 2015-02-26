from django.db import models

# Create your models here.


class CarSharingData(models.Model):
    toPlace = models.CharField(max_length=30)
    fromPlace = models.CharField(max_length=30)
    timestamp = models.DateTimeField()
    reg = models.CharField(max_length=20)


    def __unicode__(self):
        return self.city
