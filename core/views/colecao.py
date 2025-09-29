from rest_framework import viewsets
from core.models.colecao import Colecao
from core.serializers.colecao import ColecaoSerializer

class ColecaoViewSet(viewsets.ModelViewSet):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
