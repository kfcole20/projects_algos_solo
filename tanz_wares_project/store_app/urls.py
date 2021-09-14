from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('registration', views.registration),
    path('register', views.register),
    path('verify', views.verify),
    path('home', views.home),
    path('logout', views.logout),
    path('add_favorite/<int:item_id>', views.add_favorite),
    path('remove_favorite/<int:item_id>', views.remove_favorite),
    path('favorites_view', views.fav_view),
    path('cart_view', views.cart_view),
    path('add_cart/<int:item_id>', views.add_cart),
    path('remove_cart/<int:item_id>', views.remove_cart),
    path('checkout', views.checkout),
    path('verify_card', views.verify_card),
    path('success', views.success)
]