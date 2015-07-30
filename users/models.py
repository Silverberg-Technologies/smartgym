import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class SmartGymUser(models.Model):
    user = models.OneToOneField(User)
    is_instructor = models.BooleanField()
    is_moderator = models.BooleanField()

class Groupsession(models.Model):
    name = models.CharField(max_length=128)
    date_time = models.DateTimeField('date and time of session')
    location = models.CharField(max_length=128)
    instructor = models.OneToOneField(SmartGymUser, default = lambda: SmartGymUser.objects.get(id=1))
    description = models.CharField(max_length=1024)
    users_attending = models.ManyToManyField(User)
    available_slots = models.IntegerField()

    def __str__(self):
        return self.name

class Oauth2Codes(models.Model):
    user = models.OneToOneField(User)
    access_token = models.CharField(max_length=128)
    refresh_token = models.CharField(max_length=128)
    expire_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user

class LFUserProfile(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField()
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    nickName = models.CharField(max_length=255)
    gender = models.CharField(max_length=255) # Possible values: m/M - Male f/F - Female
    emailAddress = models.EmailField(max_length=254)
    height = models.FloatField()
    heightUnit = models.CharField(max_length=255) # Possible values: I - Imperial (meaning height is in inches) M - Metric (meaning height is in cms)
    weight = models.FloatField()
    weightUnit = models.CharField(max_length=255) # Possible values: I - Imperial M - Metric
    preferredUnit = models.CharField(max_length=255) # PUser's prefered unit used in the workouts, etc. Possible values: I - Imperial M - Metric
    createdOn = models.DateTimeField()


User.profile = property(lambda u: SmartGymUser.object.get_or_create(user=u)[0])
