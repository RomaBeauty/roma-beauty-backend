from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from .produto import Produto

class ItemSacola(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    adicionado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'produto')

    def __str__(self):
        return f"{self.produto.nome} - {self.user.username}"
