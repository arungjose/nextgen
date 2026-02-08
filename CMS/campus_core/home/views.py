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
