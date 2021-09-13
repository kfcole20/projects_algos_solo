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
    path('remove_favorite/<int:item_id>', views.remove_favorite)
]