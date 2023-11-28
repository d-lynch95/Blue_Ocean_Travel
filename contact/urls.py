from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('contact/', views.submitForm, name='submit'),
    path('success/', views.success, name='success'),
]