from django.db import models


class Purchase(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    sobrenome = models.CharField(max_length=100, verbose_name="Sobrenome")
    email = models.EmailField(verbose_name="E-mail")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    cep = models.CharField(max_length=9, verbose_name="CEP")
    rua = models.CharField(max_length=200, verbose_name="Rua")
    bairro = models.CharField(max_length=100, verbose_name="Bairro")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    estado = models.CharField(max_length=2, verbose_name="Estado")
    numero = models.CharField(max_length=10, verbose_name="Número")
    complemento = models.CharField(max_length=200, blank=True, null=True, verbose_name="Complemento")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.nome} {self.sobrenome} - {self.email}"