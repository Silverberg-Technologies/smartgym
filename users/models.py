import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Groupsession(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name
    date_time = models.DateTimeField('date and time of session')
    coach = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    users_attending = models.ManyToManyField(User)

class Oauth2Codes(models.Model):
    user = models.OneToOneField(User)
    access_token = models.CharField(max_length=128)
    refresh_token = models.CharField(max_length=128)
    expires_in = models.IntegerField()

    def __str__(self):
        return self.user

class LFUserProfile(models.Model):
    age = models.IntegerField()
    firstName = models.CharField()
    lasName = models.CharField()
    nickName = models.CharField()
    gender = models.CharField() # Possible values: m/M - Male f/F - Female
    emailAddress = models.EmailField(max_length=254)
    height = models.FloatField()
    heightUnit = models.CharField() # Possible values: I - Imperial (meaning height is in inches) M - Metric (meaning height is in cms)
    weight = models.FloatField()
    weightUnit = models.CharField() # Possible values: I - Imperial M - Metric
    preferredUnit = models.CharField() # PUser's prefered unit used in the workouts, etc. Possible values: I - Imperial M - Metric
    createdOn = models.DateTimeField()
