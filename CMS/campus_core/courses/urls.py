from os import name
from django.urls import path

from . import views

urlpatterns = [
    path("catalog", views.course_catalog, name='courselist'),
    path("details", views.course_details, name='coursedetails'),
    path("delete/<int:cid>", views.course_delete, name='coursedelete'),
    path("update/<int:cid>", views.course_update, name='courseupdate')
]
