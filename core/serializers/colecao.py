from rest_framework import serializers
from core.models.colecao import Colecao
from core.models.tipo import Tipo

class ColecaoSerializer(serializers.ModelSerializer):
    tipos = serializers.PrimaryKeyRelatedField(
        queryset=Tipo.objects.all(),
        many=True
    )
    tipos_nomes = serializers.StringRelatedField(source='tipos', many=True, read_only=True)

    class Meta:
        model = Colecao
        fields = ['id', 'nome', 'descricao', 'imagem_capa', 'imagem_mostruario', 'tipos', 'tipos_nomes']
