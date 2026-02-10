from django.contrib.auth.forms import UserCreationForm
from .forms import ContactForm
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, "home/index.html")


def about(request):
    return render(request, "home/about.html")


def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mainpage')

    else:
        form = ContactForm()

    return render(request, "home/contact.html", {'form': form})


def register(request):
    if request.method=='POST': # File clicking register button
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # New user will be added to auth_user
            return redirect('login')
    else: # First time when register page is loaded
        form=UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})
