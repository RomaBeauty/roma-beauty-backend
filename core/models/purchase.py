from django.db import models

class Purchase(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Total da Compra"
    )

    def __str__(self):
        return f"{self.nome} {self.sobrenome} - {self.email}"


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, related_name='itens', on_delete=models.CASCADE)
    produto_nome = models.CharField(max_length=200)
    produto_id = models.IntegerField()
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.produto_nome} x{self.quantidade}"
