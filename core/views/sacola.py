from rest_framework import viewsets, permissions
from core.models import ItemSacola
from core.serializers import ItemSacolaSerializer

class ItemSacolaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ItemSacolaSerializer

    def get_queryset(self):
        return ItemSacola.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
