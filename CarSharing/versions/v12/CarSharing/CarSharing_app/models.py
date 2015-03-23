from django.db import models
from django.contrib.auth.models import User

# Create your models here.


BOOLEAN_CHOICES = (('True', 'True label'), ('False', 'False label'))

class driver(models.Model):
  client_id = models.CharField(max_length = 30, primary_key=True)
  firstname = models.CharField(max_length = 30)
  lastname = models.CharField(max_length = 30)
  email = models.CharField(max_length = 30)
  age = models.IntegerField(max_length = 5)
  phone = models.IntegerField(max_length = 10)
  gender = models.CharField(max_length = 10)
  client_is = models.CharField(max_length = 10)
  home = models.CharField(max_length = 100)

  
  def __unicode__(self):
    return (self.client_id)
    
    
class drivers_car(models.Model):
  id_client = models.CharField(max_length = 30)
  car_reg = models.CharField(max_length = 10, primary_key=True)
  car_desc = models.CharField(max_length = 200)
  seats_free = models.CharField(max_length = 5)
  
  def __unicode__(self):
    return (self.id_client)
  
  
  
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
  driver_id = models.CharField(max_length = 30)
  journey_name = models.CharField(max_length = 30, primary_key=True)
  from_place = models.CharField(max_length = 30)
  to_place = models.CharField(max_length = 30)
  time = models.DateTimeField()
  price = models.IntegerField(max_length = 10)
  seats_free = models.IntegerField(max_length = 10)
  car_desc= models.CharField(max_length = 30)
  deviate = models.CharField(max_length = 10)
  
  def __unicode__(self):
     return (self.journey_name)
  
class requests(models.Model):
  driver_id = models.ForeignKey(driver)
  journey_name = models.ForeignKey(route)
  
  def __unicode__(self):
    return (self.driver_id, self.journey_name)
  

class clientMessages(models.Model):
  messageFrom = models.CharField(max_length = 30)
  messageTo = models.TextField()
  driverMessage = models.CharField(max_length = 30)
  time = models.DateTimeField(auto_now_add=True)
  
  def __unicode__(self):
    return (self.driver_id_sender)
  
  
  
  
  
  
  
 
  
