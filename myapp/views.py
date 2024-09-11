from django.shortcuts import render, get_object_or_404
from .models import BlogPost, UserProfile
from rest_framework import viewsets
from .serializers import BlogPostSerializer, UserProfileSerializer

# View to display all blog posts
def blog_list(request):
    posts = BlogPost.objects.filter(is_published=True).order_by('-created_at')  # Only show published posts
    return render(request, 'blog_list.html', {'posts': posts})

# View to display a single blog post
def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_detail.html', {'post': post})

# View to display a user profile
def user_profile(request, username):
    profile = get_object_or_404(UserProfile, user__username=username)
    return render(request, 'user_profile.html', {'profile': profile})

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer