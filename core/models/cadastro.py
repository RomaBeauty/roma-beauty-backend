from django.db import models


class Cadastro(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True, verbose_name=('email'), help_text=('Email'))
    senha = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
