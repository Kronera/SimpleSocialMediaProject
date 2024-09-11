from django.contrib import admin
from .models import BlogPost, UserProfile

# Register the BlogPost model
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'is_published')
    search_fields = ('title', 'user__username')
    list_filter = ('is_published', 'created_at')
    ordering = ('-created_at',)

# Register the UserProfile model
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location')
    search_fields = ('user__username', 'location')
