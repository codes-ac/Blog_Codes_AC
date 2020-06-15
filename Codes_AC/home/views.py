from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from blog.models import Post

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        if len(name)<2 or len(email)<4 or len(phone)<10 or len(desc)<5:
            messages.warning(request,'Fill the form correctly...')
        else:
            contact = Contact(name=name, email=email, phone=phone, desc=desc)
            contact.save()
            messages.success(request,'Succesfully submitted...')

    return render(request, 'home/contact.html')


def search(request):
    search = request.GET['query']
    if len(search)==0:
        messages.warning(request,"You have not entered anything in search box, please refine your search...")
        post = []
    else:
        if len(search)>50:
            messages.warning(request,"Entered text size is too large, please refine your search...")
            post = []
        else:
            postTitle = Post.objects.filter(title__icontains=search)
            postContent = Post.objects.filter(content__icontains=search)
            post = postTitle.union(postContent)
    return render(request, 'home/seacrh.html', {'post':post, 'query':search})
