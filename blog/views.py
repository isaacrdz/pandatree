from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Post
from models import *


def blog(request):
	posts = Post.objects.all()
	template = 'blog.html'
	return render(request,template,{'posts':posts,'request':request})

def blog_view(request, slug):
	post = get_object_or_404(Post, slug = slug)
	template = 'post.html'
	return render(request,template,{'post':post,})

