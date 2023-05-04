from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('perfil', views.perfil, name="perfil"),
    path('criartarefa', views.criartarefa, name="criartarefa"),
    path('salvar', views.salvar, name="salvar"),
    path('updatetarefa/<int:id>', views.updatetarefa, name="updatetarefa"),
    path('update/<int:id>', views.update, name="update"),
    path('deletetarefa/<int:id>', views.deletetarefa, name="deletetarefa"),
    path('delete/<int:id>', views.delete, name="delete") 
]

