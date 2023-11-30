from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_view, name='staff'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_view/<int:product_id>/', views.delete_view, name='delete_view'),
    path('delete/<int:product_id>/', views.delete_product.as_view(), name='delete_product'),
]
