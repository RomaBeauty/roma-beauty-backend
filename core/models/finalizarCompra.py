
from django.db import models


class FinalizarCompra(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    telefone = models.CharField(max_length=15)
    numero = models.CharField(max_length=10)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.nome} - {self.cep}'
