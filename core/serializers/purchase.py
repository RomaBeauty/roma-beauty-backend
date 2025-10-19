from rest_framework import serializers
from ..models.purchase import Purchase, PurchaseItem

class PurchaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseItem
        # produto é FK no modelo, então aqui usamos 'produto' ou 'produto_id'
        fields = ['produto_id', 'produto_nome', 'quantidade', 'preco_unitario']


class PurchaseSerializer(serializers.ModelSerializer):
    itens = PurchaseItemSerializer(many=True)  # campo aninhado
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)  # calculado


    class Meta:
        model = Purchase
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'total']

    def create(self, validated_data):
        itens_data = validated_data.pop('itens', [])
        purchase = Purchase.objects.create(**validated_data)

        total_calculado = 0
        for item in itens_data:
            preco_item = item.get('preco_unitario', 0)
            quantidade = item.get('quantidade', 1)
            total_calculado += preco_item * quantidade

            PurchaseItem.objects.create(
                purchase=purchase,
                produto_id=item['produto_id'],
                produto_nome=item['produto_nome'],
                quantidade=quantidade,
                preco_unitario=preco_item
            )

        # Atualiza o total na compra
        purchase.total = total_calculado
        purchase.save()

        return purchase
