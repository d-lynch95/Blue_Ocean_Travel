from django.urls import path
from . import views

urlpatterns = [
    path("", views.WishList.as_view(), name="wishlist"),
    path('addwish/<int:item_id>/', views.add_to_wishlist, name='addwish'),
]