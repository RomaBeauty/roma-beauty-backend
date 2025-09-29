from django.db import models
from core.models.category import Category 

class Tipo(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="tipos"  
    )

    def __str__(self):
        return f"{self.nome} ({self.categoria.nome})"
def get_default_categoria():
    from core.models.category import Category
    categoria, _ = Category.objects.get_or_create(
        nome="OUTROS",
        defaults={'descricao': 'Categoria padrão para tipos não classificados'}
    )
    return categoria.id

class Tipo(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="tipos",
        default=get_default_categoria   # 👈 sempre usa “Outros” se não informar
    )

    def __str__(self):
        return f"{self.nome} ({self.categoria.nome})"
