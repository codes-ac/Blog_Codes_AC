from django.shortcuts import render
from .models import Post

def blogHome(request):
    
    post = Post.objects.all()
    return render(request, 'blog/blogHome.html',{'posts':post})

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug)
    return render(request, 'blog/blogPost.html',{'post':post})