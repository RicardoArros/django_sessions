from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, "index.html")
  
def home(request):
    return render(request, "home.html")
  
def create(request):
    return render(request, "crud/create.html")