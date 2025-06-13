from rest_framework.serializers import ModelSerializer
from core.models import FinalizarCompra


class FinalizarCompraSerializer(ModelSerializer):
    class Meta:
        model = FinalizarCompra
        fields = [
            'id', 'nome', 'email', 'telefone', 'numero',
            'endereco', 'cidade', 'estado', 'cep', 'complemento'
        ]
