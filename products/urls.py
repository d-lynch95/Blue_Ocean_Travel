from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
]
