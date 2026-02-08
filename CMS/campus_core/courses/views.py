from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Courses
from .forms import CourseForm

# Create your views here.
def course_catalog(request):

    courses = ["Bachelor's in Engineering", "Master's in Engineering", "Bachelor's in Science", "Master's in Science", "Bachelor's in Arts", "Master's in Arts"]
    count = {"UG":4, "PG":4}

    return render(request, "courses/catalogger.html", {"courses":courses, "count":count})

    # return HttpResponse("<h1>Browse your available courses here</h1>")

def course_details(request):
    data = Courses.objects.all()
    return render(request, "courses/details.html", {"details":data})

def course_delete(request, cid):
    record=Courses.objects.get(id=cid)
    record.delete()
    return redirect('coursedetails')

def course_update(request, cid):
    record = Courses.objects.get(id=cid)
    if request.method=='GET':
        forms=CourseForm(instance=record)
        return render(request, 'courses/courseupdate.html', {'form':forms})
    else:
        form=CourseForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
        return redirect('coursedetails')
