from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about_us, name='aboutus'),
    path('privacy/', views.about_us, name='privacy'),
]
