from os import name
from django.urls import path
from . import views

urlpatterns = [
    path("list", views.student_list, name='studentlist'),
    path("form", views.student_form),
    path('delete/<int:sid>', views.student_delete, name='delete_student'),
    path('update/<int:sid>', views.student_update, name='update_Student')
]
