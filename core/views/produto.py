# core/views/produto.py
from rest_framework import viewsets
from core.models.produto import Produto
from core.serializers.produto import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.select_related('category', 'colecao', 'tipo').all()
    serializer_class = ProdutoSerializer
