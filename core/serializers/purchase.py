from rest_framework import serializers
from ..models.purchase import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        
    def validate_cep(self, value):
        # Remove caracteres especiais do CEP
        cep = value.replace('-', '').replace(' ', '')
        
        if len(cep) != 8 or not cep.isdigit():
            raise serializers.ValidationError("CEP deve ter 8 dígitos numéricos")
        
        return cep
    
    def validate_email(self, value):
        # Validação adicional de email se necessário
        if Purchase.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email já está cadastrado")
        
        return value