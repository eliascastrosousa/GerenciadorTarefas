# GerenciadorTarefas

Projeto de CRUD com autenticação, para criar tarefas, marca-los como feitos, arquiva-los e deixar sua resenha.
Usuario admin tem permissão de adicionar a tarefas a outros usuarios.

Para abrir o Projeto 
~~~powershell
  git clone https://github.com/eliascastrosousa/GerenciadorTarefas.git .
~~~
Crie um ambiente virtual 
~~~powershell
  python -m venv env
~~~
Ative
~~~powershell
  .\env\scripts\activate
~~~

Instale o Framework Django

~~~powershell
  pip install django
~~~
Rode o comando agora para verificar se há migrações a serem feitas pelo django

~~~powershell
  python manage.py migrate
~~~

Agora é só rodar o projeto

~~~powershell 
  python manage.py runserver
~~~

Este projeto está em contrução. sinta-se livre para realizar novas melhorias. toda ajuda é bem vinda. :)
                                                                                                                                                                       
