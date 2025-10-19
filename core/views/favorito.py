from rest_framework import viewsets, permissions, serializers
from rest_framework.permissions import IsAuthenticated
from core.models import Favorito, Produto
from core.serializers import FavoritoSerializer
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

class FavoritoViewSet(viewsets.ModelViewSet):
    serializer_class = FavoritoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorito.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        produto_id = self.request.data.get("produto_id")
        if not produto_id:
            raise serializers.ValidationError({"produto_id": "Este campo é obrigatório."})
        try:
            produto = Produto.objects.get(id=produto_id)
        except Produto.DoesNotExist:
            raise serializers.ValidationError({"produto_id": "Produto não encontrado."})
        serializer.save(user=self.request.user, produto=produto)

