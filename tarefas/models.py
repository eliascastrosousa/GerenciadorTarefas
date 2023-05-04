from django.db import models


class Lista(models.Model):
    titulotarefa = models.CharField(max_length=100)
    comentario = models.TextField()
    urgencia = models.CharField(max_length=100)
    dataatribuicao = models.DateField()
    datafinalizacao = models.DateField()
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return self.titulotarefa
