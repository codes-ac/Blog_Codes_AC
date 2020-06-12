from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.blogHome, name="Blog Home"),
    path('<str:slug>/', views.blogPost, name="Blog Post")
]