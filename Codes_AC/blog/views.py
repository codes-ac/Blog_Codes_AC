from django.shortcuts import render
from .models import Post

def blogHome(request):
    
    post = Post.objects.all()

    return render(request, 'blog/blogHome.html',{'posts':post})

def blogPost(request, slug):
    return render(request, 'blog/blogPost.html')