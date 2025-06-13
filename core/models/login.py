from django.db import models


class Login(models.Model):
    nome = models.CharField(max_length=150)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome