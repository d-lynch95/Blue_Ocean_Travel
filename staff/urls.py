from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_view, name='staff'),
    path('view_forms/', views.ContactList.as_view(), name='view_forms'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
