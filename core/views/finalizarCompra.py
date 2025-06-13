from rest_framework.viewsets import ModelViewSet

from core.models import FinalizarCompra
from core.serializers import FinalizarCompraSerializer


class FinalizarCompraViewSet(ModelViewSet):
    queryset = FinalizarCompra.objects.all()
    serializer_class = FinalizarCompraSerializer
