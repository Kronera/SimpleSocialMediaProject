from django.contrib import admin
from .models import UserProfile, BlogPost

# Register the models to be accessible in the admin panel
admin.site.register(UserProfile)
admin.site.register(BlogPost)
