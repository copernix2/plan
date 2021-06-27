from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.indexDash, name='home'),
    path('', views.dashboard, name='dashboard'),
    path('dossier', views.dashboard, name='dossierfemme'),
    path('ac-folder/<str:ac>/', views.acFolder, name='dossierac'),
    path('search/', views.search, name='search'),
    path('woman-folder/<str:ac>/<str:femme>/', views.womanFolder, name='woman-folder'),
]

