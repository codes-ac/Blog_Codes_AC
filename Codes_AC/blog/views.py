from django.shortcuts import render, redirect
from .models import Post, BlogComment
from django.contrib import messages

def blogHome(request):
    
    post = Post.objects.all()
    return render(request, 'blog/blogHome.html',{'posts':post})


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug)
    comments = BlogComment.objects.filter(post=post[0])
    return render(request, 'blog/blogPost.html',{'post':post, 'comments':comments})
    

def postComment(request):
    if request.method == 'POST': 
        comment = request.POST.get('comment')
        user = request.user
        postId = request.POST.get('postId')
        post = Post.objects.get(sno=postId)

        comment = BlogComment(comment=comment, user=user, post=post)
        comment.save()

        messages.warning(request, "comment added")

        return redirect(f"/blog/{post.slug}")
    