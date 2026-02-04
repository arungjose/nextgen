from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def student_list(request):

    std_record = [{'slno':1, 'name':'Adarsh', 'course':'cs'},{'slno':2, 'name':'Arun', 'course':'cs'},{'slno':3, 'name':'Arjun', 'course':'cs'}]

    data = {"admission_closed": False, "count": 63, "students":std_record}

    return render(request, "students/studentlist.html", {"adm_data": data})
    # return HttpResponse("<h1>WELCOME TO THE STUDENT DIRECTORY</h1>")
