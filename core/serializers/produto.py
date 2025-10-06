from rest_framework import serializers
from core.models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    descricao_colecao = serializers.ReadOnlyField()
    imagem_mostruario_colecao = serializers.ReadOnlyField()

    class Meta:
        model = Produto
        fields = [
            'id',
            'nome',
            'preco',
            'imagem',
            'categoria',
            'colecao',
            'tipo',
            'descricao_colecao',
            'imagem_mostruario_colecao',
        ]
