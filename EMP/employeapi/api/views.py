from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Employee
from .serializers import EmployeeSerializer


# Create your views here.
def home(request):
    return HttpResponse("Home Page")

def emp_all(request):
    records=Employee.objects.all()
    print(records)
    serializer=EmployeeSerializer(records, many=True)
    print(serializer.data)
    return JsonResponse(serializer.data, safe=False)

def emp_one(request, id):
    record=Employee.objects.get(id=id)
    return HttpResponse(record)

def emp_create(request):
    pass
