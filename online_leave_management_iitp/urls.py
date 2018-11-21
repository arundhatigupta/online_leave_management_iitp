from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
