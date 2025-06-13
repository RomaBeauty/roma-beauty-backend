from rest_framework.viewsets import ModelViewSet

from core.models import Login
from core.serializers import LoginSerializer


class LoginViewSet(ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
