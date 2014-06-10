from django.shortcuts import render,get_object_or_404
from .models import Blog

# Create your views here.
def blog(request, slug):
	blog = get_object_or_404(Blog, slug = slug)
	template = "blog.html"
	return render(request,template,{"blog":blog, "request":request})