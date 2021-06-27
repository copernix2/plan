from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('dashboard/', include('dashboard.urls')),
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
    #path('accounts/', include('django.contrib.auth.urls')),
]
