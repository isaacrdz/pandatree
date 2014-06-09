from django.shortcuts import render
from .models import Service

# Create your views here.
def home(request):
	services = Service.objects.all()
	template = 'index.html'
	return render(request,template,{"services":services,"request":request})