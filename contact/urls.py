from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('contactforms/', views.ContactList.as_view(), name="ContactList"),
    path('submitform/', views.SubmitForm.as_view(), name='submitform'),

]