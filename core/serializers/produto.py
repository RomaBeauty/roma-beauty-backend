# core/serializers/produto.py
from rest_framework import serializers
from core.models.produto import Produto
from core.models.colecao import Colecao
from core.models.tipo import Tipo
from core.models.category import Category

class ColecaoNestedSerializer(serializers.ModelSerializer):
    imagem_mostruario = serializers.SerializerMethodField()

    class Meta:
        model = Colecao
        fields = ['id', 'nome', 'descricao', 'imagem_mostruario']

    def get_imagem_mostruario(self, obj):
        request = self.context.get('request')
        if obj.imagem_mostruario:
            return request.build_absolute_uri(obj.imagem_mostruario.url)
        return None

class TipoNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ['id', 'nome']

class CategoryNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # ajuste esses campos conforme seu model Category
        fields = ['id', 'nome']

class ProdutoSerializer(serializers.ModelSerializer):
    imagem_produto = serializers.SerializerMethodField()
    imagem_amostra = serializers.SerializerMethodField()
    colecao = ColecaoNestedSerializer(read_only=True)
    tipo = TipoNestedSerializer(read_only=True)
    category = CategoryNestedSerializer(read_only=True)  # campo chamado "category" no model
    descricao_colecao = serializers.ReadOnlyField()  # chama o property do model

    class Meta:
        model = Produto
        fields = [
            'id', 'nome', 'preco',
            'imagem_produto', 'imagem_amostra',
            'colecao', 'tipo', 'category',
            'descricao_colecao',
        ]

    def get_imagem_produto(self, obj):
        request = self.context.get('request')
        if obj.imagem_produto:
            return request.build_absolute_uri(obj.imagem_produto.url)
        return None

    def get_imagem_amostra(self, obj):
        request = self.context.get('request')
        if obj.imagem_amostra:
            return request.build_absolute_uri(obj.imagem_amostra.url)
        return None
