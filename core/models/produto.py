from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem_produto = models.ImageField(upload_to='produtos/', blank=True, null=True)
    imagem_amostra = models.ImageField(upload_to='amostras/', blank=True, null=True)

    category = models.ForeignKey(
        'core.Category',  # 👈 referência correta
        on_delete=models.CASCADE,
        related_name='produtos'
    )

    colecao = models.ForeignKey(
        'Colecao',
        on_delete=models.CASCADE,
        related_name='produtos'
    )

    tipo = models.ForeignKey(
        'Tipo',
        on_delete=models.CASCADE,
        related_name='produtos'
    )

    def __str__(self):
        return self.nome

    @property
    def descricao_colecao(self):
        return self.colecao.descricao if self.colecao else None

    @property
    def imagem_mostruario_colecao(self):
        return (
            self.colecao.imagem_mostruario.url
            if self.colecao and self.colecao.imagem_mostruario
            else None
        )
