from django.db import models

# Create your models here.
class Service(models.Model):
	category = models.CharField(max_length = 50)
	description = models.TextField(blank = True)

	def __unicode__(self):
		return self.category