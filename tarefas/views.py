from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.decorators import login_required

@login_required(login_url="/auth/login/")
def home(request):
    return render(request, 'home.html')

@login_required(login_url="/auth/login/")
def perfil(request):
    return render(request, 'perfil.html')