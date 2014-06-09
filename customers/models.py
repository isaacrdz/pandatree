from django.db import models
from services.models import Service

# Create your models here.
class Customer(models.Model):
	name = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 70)
	phone_number = models.IntegerField(default = 0)
	service = models.ForeignKey(Service)
	description = models.TextField(blank = True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.name
