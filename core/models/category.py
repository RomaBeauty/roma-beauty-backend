from django.db import models

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('MAQUIAGEM', 'Maquiagem'),
        ('SKINCARE', 'SkinCare'),
        ('CABELO', 'Cabelo'),
        ('OUTROS', 'Outros'),
    ]

    nome = models.CharField(max_length=20, choices=CATEGORY_CHOICES, unique=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
