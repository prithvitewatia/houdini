from django.shortcuts import render
from .models import *


def home(request):
    posts = Post.objects.all()
    context = {
        "pageTitle": "Blogs",
        "posts": posts
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html')
