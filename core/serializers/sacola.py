from rest_framework import serializers
from core.models import ItemSacola

class ItemSacolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSacola
        fields = '__all__'
