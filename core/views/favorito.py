from rest_framework import viewsets, permissions
from core.models import Favorito
from core.serializers import FavoritoSerializer

class FavoritoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FavoritoSerializer

    def get_queryset(self):
        return Favorito.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
