from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse("<h2>Hello from django</h2>")


def about(request):
    return HttpResponse(
        "<marquee><h1>This is the ABOUT PAGE HEHEHEHEHEHEHEHEHEHEHE</h1></marquee>"
    )
