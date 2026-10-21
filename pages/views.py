from django.shortcuts import render
from pages.namer import namer

def home(request):
    return render(request, "home.html", {})

def about(request):
    return render(request, "about.html", {"my_stuff":namer})
