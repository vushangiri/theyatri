from django.db import models
from django.utils import timezone

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default = False)
    sittayma = models.BooleanField(default= True)
    video = models.URLField(max_length=500)
class passhash(models.Model):
    salt = models.CharField(max_length=200)
    user = models.CharField(max_length=200)

class contact(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    subject = models.TextField()
    email = models.EmailField()
    message = models.TextField()
class subscribe(models.Model):
    name = models.TextField()
    email = models.EmailField()
class bookings(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    plocation = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    hour = models.CharField(max_length=100)
    min = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)






















