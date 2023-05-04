from . import views
from django.urls import path
from .views import *


urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro' ),
    path('login/', views.login, name='login' ),
    path('plataforma/', views.plataforma, name='plataforma' ),
    path('deslogar_usuario/', deslogar_usuario, name='deslogar_usuario'),

    
]