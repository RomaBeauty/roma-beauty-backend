from rest_framework.viewsets import ModelViewSet

from core.models import Cadastro
from core.serializers import CadastroSerializer


class CadastroViewSet(ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer
