from rest_framework import serializers
from core.models.tipo import Tipo
from core.models.category import Category

class TipoSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.CharField(source='categoria.nome', read_only=True)

    class Meta:
        model = Tipo
        fields = ['id', 'nome', 'descricao', 'categoria', 'categoria_nome']
