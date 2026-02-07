from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

# Create your views here
def student_form(request):
    if request.method=="GET":
        form=StudentForm()
        return render(request, "students/studentform.html", {'form':form})
    else: # When form is submitted /students/form is called in POST
        form=StudentForm(request.POST) # Filled Form
        if form.is_valid(): # Checking id form is valid
            form.save() # Make changed to db
        return redirect("studentlist")

def student_list(request):
    data=Student.objects.all()
    return render(request, "students/studentlist.html", {"data": data, "count":len(data)})

def old_student_list(request):
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


def student_delete(request, sid):
    record=Student.objects.get(id=sid) # Select * FROM student WHERE id=sid
    record.delete()
    return redirect("studentlist")

def student_update(request, sid):
    record=Student.objects.get(id=sid)
    if request.method=='GET':
        form=StudentForm(instance=record) #Filled form with selected student record
        return render(request, 'students/update_form.html', {'form':form})
    else:
        form=StudentForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
        return redirect('studentlist')
