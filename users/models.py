import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Groupsession(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name
	date_time = models.DateTimeField('date and time of session')
	coach = models.CharField(max_length=100)
	description = models.CharField(max_length=1024)
	users_attending = models.ManyToManyField(User)