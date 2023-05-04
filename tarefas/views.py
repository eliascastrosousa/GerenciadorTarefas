from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Lista


@login_required(login_url="/auth/login/")
def home(request):
    lista_tarefas = Lista.objects.all()
    return render(request, 'home.html', {"lista":lista_tarefas})

@login_required(login_url="/auth/login/")
def perfil(request):
    return render(request, 'perfil.html')

@login_required(login_url="/auth/login/")
def criartarefa(request):
    return render(request, 'criartarefa.html')

@login_required(login_url="/auth/login/")
def salvar(request):
    titulotarefa = request.POST.get('titulotarefa')
    comentario = request.POST.get('comentario')
    urgencia = request.POST.get('urgencia')
    dataatribuicao = datetime.now()
    datafinalizacao = request.POST.get('datafinalizacao')

    lista_tarefas = Lista.objects.all()
    Lista.objects.create(titulotarefa = titulotarefa, 
                        comentario = comentario, 
                        urgencia = urgencia,
                        dataatribuicao = dataatribuicao,
                        datafinalizacao = datafinalizacao)
    
    return render(request, 'home.html', {"lista":lista_tarefas})

@login_required(login_url="/auth/login/")
def updatetarefa(request, id):
    lista_tarefas = Lista.objects.get(id=id)
    return render(request, 'updatetarefa.html', {"lista":lista_tarefas})

@login_required(login_url="/auth/login/")
def update(request, id):
    lista_tarefas = Lista.objects.get(id=id)
    return render(request, 'updatetarefa.html', {"lista":lista_tarefas})

@login_required(login_url="/auth/login/")
def deletetarefa(request, id):
    lista_tarefas = Lista.objects.get(id=id)
    return render(request, 'deletetarefa.html', {"lista":lista_tarefas})

@login_required(login_url="/auth/login/")
def delete(request, id):
    lista = Lista.objects.get(id=id)
    lista.delete()
    return redirect(home)