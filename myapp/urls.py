from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blog_list, name='blog_list'),  # List of all blogs
    path('blogs/<int:pk>/', views.blog_detail, name='blog_detail'),  # Detail of a specific blog post
    path('profile/<str:username>/', views.user_profile, name='user_profile'),  # User profile by username
]
