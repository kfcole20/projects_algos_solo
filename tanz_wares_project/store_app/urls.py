from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('registration', views.registration),
    path('register', views.registration),
    path('verify', views.verify),
]