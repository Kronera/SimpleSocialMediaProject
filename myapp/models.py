from django.db import models
from django.contrib.auth.models import User

# Model for user profiles
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to the built-in User model
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Optional profile picture

    def __str__(self):
        return self.user.username


# Model for blog posts
class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Each post is tied to a user
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)  # You can mark posts as published or drafts

    def __str__(self):
        return self.title
