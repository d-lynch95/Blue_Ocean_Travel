from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('submitform/', views.SubmitForm.as_view(), name='submitform'),
]