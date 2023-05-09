from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Lista


@login_required(login_url="/auth/login/")
def home(request):
    lista_tarefas = Lista.objects.filter(useratribuido = request.user.username, concluido=False)
    return render(request, 'home.html', {"lista":lista_tarefas})

@login_required(login_url="/auth/login/")
def perfil(request):
    return render(request, 'perfil.html')

@login_required(login_url="/auth/login/")
def criartarefa(request):
    users = User.objects.all()
    return render(request, 'criartarefa.html', {'users': users})

@login_required(login_url="/auth/login/")
def salvar(request):
    titulotarefa = request.POST.get('titulotarefa')
    comentario = request.POST.get('comentario')
    urgencia = request.POST.get('urgencia')
    username = request.user.username
    useratribuido = request.POST.get('user_atribuido')
    dataatribuicao = datetime.now()
    datafinalizacao = request.POST.get('datafinalizacao')

    lista_tarefas = Lista.objects.all()
    Lista.objects.create(titulotarefa = titulotarefa, 
                        comentario = comentario, 
                        urgencia = urgencia,
                        dataatribuicao = dataatribuicao,
                        datafinalizacao = datafinalizacao,
                        useratribuido = useratribuido,
                        username = username
                        )
    
    return redirect(home)

@login_required(login_url="/auth/login/")
def updatetarefa(request, id):
    lista_tarefas = Lista.objects.get(id=id)
    return render(request, 'updatetarefa.html', {"lista":lista_tarefas})

@login_required(login_url="/auth/login/")
def update(request, id):
    lista = Lista.objects.get(id=id)
    
    if request.POST.get("titulotarefa"):
        lista.titulotarefa = request.POST.get("titulotarefa")

    if request.POST.get("comentario"):
        lista.comentario = request.POST.get("comentario")

    if request.POST.get("user_atribuido"):
        lista.useratribuido = request.POST.get("user_atribuido")

    if request.POST.get("concluido"):
        lista.concluido = True
        lista.datafinalizacao = datetime.now()
    
    lista.save()
    return redirect(home) 

@login_required(login_url="/auth/login/")
def deletetarefa(request, id):
    lista_tarefas = Lista.objects.get(id=id)
    return render(request, 'deletetarefa.html', {"lista":lista_tarefas})

@login_required(login_url="/auth/login/")
def delete(request, id):
    lista = Lista.objects.get(id=id)
    lista.delete()
    return redirect(home)

@login_required(login_url="/auth/login/")
def tarefasconcluidas(request):
    lista_tarefas = Lista.objects.filter(useratribuido = request.user.username, concluido=True)
    return render(request, 'tarefasconcluidas.html', {"lista":lista_tarefas})


