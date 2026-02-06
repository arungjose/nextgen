from os import name
from django.urls import path

from . import views

urlpatterns = [path("list", views.student_list, name='studentlist'),path("form", views.student_form)]
