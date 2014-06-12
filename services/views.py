from django.shortcuts import render
from .models import Service
from models import *
from blog.models import Post
# Create your views here.

def home(request):
	posts = Post.objects.all()
	template = "index.html"
	return render(request,template,{'posts':posts})

	
def services(request):
	services = Service.objects.all()
	template = 'services.html'
	return render(request,template,{"services":services,"request":request})