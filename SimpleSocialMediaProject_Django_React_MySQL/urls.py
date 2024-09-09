from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('', include('myapp.urls')),  # Include your app's URLs (replace 'myapp' with the name of your app)
]