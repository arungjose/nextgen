from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.home),
    path('employees/', views.emp_all, name='emp_all'),
    path('employees/<int:id>', views.emp_one, name='emp_one'),
    path('employees/', views.emp_create, name='emp_create'),
]
