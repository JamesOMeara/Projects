from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CarSharingData(models.Model):
  fromPlace = models.CharField(max_length=30)
  toPlace = models.CharField(max_length=30)
  time = models.DateTimeField()
  reg = models.CharField(max_length=30)
  seats_free = models.IntegerField(max_length = 10)

  def __unicode__(self):
    return self.fromPlace
    

class RouteData(models.Model):
  fromPlace = models.CharField(max_length=30)
  toPlace = models.CharField(max_length=30)
  time = models.DateTimeField()
  reg = models.CharField(max_length=30)

  def __unicode__(self):
    return self.fromPlace



class driver(models.Model):
  driver_id = models.CharField(max_length = 30, primary_key=True)
  firstname = models.CharField(max_length = 30)
  lastname = models.CharField(max_length = 30)
  email = models.CharField(max_length = 30)
  age = models.IntegerField(max_length = 5)
  phone = models.IntegerField(max_length = 10)
  gender = models.CharField(max_length = 30)
  home = models.CharField(max_length = 100)
  car_reg = models.CharField(max_length = 10)
  car_desc = models.CharField(max_length = 200)
  seats_free = models.CharField(max_length = 5)
  
  def __unicode__(self):
    return (self.driver_id)
  
class passanger(models.Model):
  passanger_id = models.CharField(max_length = 30)
  firstname = models.CharField(max_length = 30)
  lastname = models.CharField(max_length = 30)
  password = models.CharField(max_length = 30)
  email = models.CharField(max_length = 30)
  age = models.IntegerField(max_length = 5)
  phone = models.IntegerField(max_length = 10)
  gender = models.CharField(max_length = 30)
  home = models.CharField(max_length = 100)
  
  def __unicode__(self):
    return (self.passanger_id)
  
class route(models.Model):
  journey_name = models.CharField(max_length = 30)
  from_place = models.CharField(max_length = 30)
  to_place = models.CharField(max_length = 30)
  time = models.DateTimeField()
  price = models.IntegerField(max_length = 10)
  seats_free = models.IntegerField(max_length = 10)
  car_desc= models.CharField(max_length = 30)
  deviate = models.BooleanField(default = True)
  
  def __unicode__(self):
     return (self.journey_name)
  
class requests(models.Model):
  driver_id = models.ForeignKey(driver)
  journey_name = models.ForeignKey(route)
 
  def __unicode__(self):
    return (self.driver_id, self.journey_name)
