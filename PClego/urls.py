from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('collector.urls')),
    path('', include('parser.urls')),
    path('', include('users.urls')),
]
