from django.db import models
from django.core.files import File  # you need this somewhere
import urllib

class Employee(models.Model):

	name = models.CharField(max_length=10,null=True)
	file = models.ImageField(upload_to='image/',blank=True)

	def __unicode__(self):
		return self.name
