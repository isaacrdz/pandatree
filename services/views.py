from django.shortcuts import render
from .models import Service

# Create your views here.

def home(request):
	template = "index.html"
	return render(request,template)

	
def services(request):
	services = Service.objects.all()
	template = 'services.html'
	return render(request,template,{"services":services,"request":request})