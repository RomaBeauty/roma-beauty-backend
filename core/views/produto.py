# core/views/produto.py
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models.produto import Produto
from core.serializers.produto import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.select_related('category', 'colecao', 'tipo').all()
    serializer_class = ProdutoSerializer

class ProdutoDetail(APIView):
    def get(self, request, pk):
        produto = Produto.objects.get(pk=pk)
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)