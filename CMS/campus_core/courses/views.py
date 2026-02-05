from django.http import HttpResponse
from django.shortcuts import render
from .models import Courses

# Create your views here.
def course_catalog(request):

    courses = ['Computer Science', 'Artificial Intelligence', 'Electrical and Electronics', 'Electronics and Communications', 'Mechanical Engineering', 'Food Technology']
    count = {"UG":4, "PG":4}

    return render(request, "courses/catalogger.html", {"courses":courses, "count":count})

    # return HttpResponse("<h1>Browse your available courses here</h1>")

def course_details(request):
    data = Courses.objects.all()
    return render(request, "courses/details.html", {"details":data})
