from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
	titulo = models.CharField(max_length= 50 )
	timestamp = models.DateTimeField(auto_now_add=True)
	imagen = models.ImageField(upload_to = 'blogs')
	contenido = models.TextField(blank = True)
	slug = models.SlugField(max_length=100)


	def __unicode__(self):
		return self.titulo
