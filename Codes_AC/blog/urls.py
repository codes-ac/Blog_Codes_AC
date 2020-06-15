from django.urls import path
from . import views
from django.contrib import admin    

urlpatterns = [
    
    path('', views.blogHome, name="blogHome"),
    path('<str:slug>', views.blogPost, name="blogPost")
]