from django.db import models
from core.models.tipo import Tipo

class Colecao(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)
    imagem_capa = models.ImageField(upload_to='colecoes/capas/', blank=True, null=True)
    imagem_mostruario = models.ImageField(upload_to='colecoes/mostruarios/', blank=True, null=True)
    tipos = models.ManyToManyField(Tipo, related_name="colecoes")  # 👈 pode ter vários tipos em uma coleção

    def __str__(self):
        return self.nome
