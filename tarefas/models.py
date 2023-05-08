from django.db import models


class Lista(models.Model):
    titulotarefa = models.CharField(max_length=100)
    comentario = models.TextField()
    urgencia = models.CharField(max_length=100)
    useratribuido = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    dataatribuicao = models.DateTimeField()
    datafinalizacao = models.DateTimeField()
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return self.titulotarefa
