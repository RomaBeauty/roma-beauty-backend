from rest_framework import viewsets
from core.models.tipo import Tipo
from core.serializers.tipo import TipoSerializer

class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer
