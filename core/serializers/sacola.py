from rest_framework import serializers
from core.models import ItemSacola, Produto

class ProdutoSacolaSerializer(serializers.ModelSerializer):
    """Serializer reduzido apenas com o que precisa aparecer na sacola."""
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco', 'imagem_produto']

class ItemSacolaSerializer(serializers.ModelSerializer):
    produto = ProdutoSacolaSerializer(read_only=True)
    produto_id = serializers.PrimaryKeyRelatedField(
        queryset=Produto.objects.all(), source='produto', write_only=True
    )

    class Meta:
        model = ItemSacola
        fields = ['id', 'produto', 'produto_id', 'quantidade']
