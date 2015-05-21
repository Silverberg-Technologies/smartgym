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
	user_id = models.OneToOneField(User, primary_key=True)
	access_token = models.CharField(max_length=128)
	refresh_token = models.CharField(max_length=128)
	expires_in = models.IntegerField()

	def __str__(self):
			return self.user_id