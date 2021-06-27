#from django.contrib import admin
from django.urls import path
from . import views 
from accounts.views import changerpassword

urlpatterns = [
    path('', views.indexhome, name='connect'),
    path('logout', views.logout_views, name='logout'),
    path('password/',changerpassword.as_view(template_name='accounts/change-password.html'), name="password"),
   
]
