from rest_framework import serializers
from core.models import Favorito, Produto
from core.serializers import ProdutoSerializer  # se estiver em outro arquivo, importe corretamente

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco', 'imagem_produto']

class FavoritoSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)  # envia o produto completo

    class Meta:
        model = Favorito
        fields = ['id', 'produto', 'adicionado_em']