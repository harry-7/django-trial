from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Signup(models.Model):
	email = models.EmailField(blank=False,null=False,primary_key=True)
	full_name = models.CharField(max_length=80)
	date_joined = models.DateTimeField(auto_now_add=True,auto_now=False)
	password = models.CharField(max_length=20)

	def __unicode__(self):
		return str(self.email)