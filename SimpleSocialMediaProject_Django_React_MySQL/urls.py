from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework import routers
from myapp import views

router = routers.DefaultRouter()
router.register(r'blogs', views.BlogPostViewSet)
router.register(r'profiles', views.UserProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),  # Admin panel URL
    path('', include('myapp.urls')),  # Include your app's URLs (replace 'myapp' with the name of your app)
    path('', TemplateView.as_view(template_name="index.html")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
