from os import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name='mainpage'),
    path("about/", views.about),
    path("contact/", views.contact, name='contactpage'),
]
