from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def student_list(request):

   std_record = [
       {'slno': 1, 'name': 'Arun Kumar', 'course': 'Computer Science'},
       {'slno': 2, 'name': 'Priya Sharma', 'course': 'Computer Science'},
       {'slno': 3, 'name': 'Rahul Nair', 'course': 'Mechanical Engineering'},
       {'slno': 4, 'name': 'Sneha Patel', 'course': 'Mechanical Engineering'},
       {'slno': 5, 'name': 'John Doe', 'course': 'Electrical Engineering'},
       {'slno': 6, 'name': 'Anita Desai', 'course': 'Electrical Engineering'}
   ]
   data = {"admission_closed": False, "count": 63, "students":std_record}
   return render(request, "students/studentlist.html", {"adm_data": data})
    # return HttpResponse("<h1>WELCOME TO THE STUDENT DIRECTORY</h1>")
