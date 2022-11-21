from django.shortcuts import render
from django.contrib.auth import logout
from .models import AppAdministracion_InsumosOficina, AppAdministracion_Vehiculos, AppAdministracion_InsumosComputacionales, AppAdministracion_Usuarios

# Create your views here.

def login(request):
  return render(request, "index.html")
  
def home(request):
  return render(request, "home.html")
  
def create(request):
  return render(request, "crud/create.html")

def list(request):
  return render(request, "crud/list.html")