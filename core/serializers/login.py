
from rest_framework.serializers import ModelSerializer
from core.models import Login


class LoginSerializer(ModelSerializer):
    class Meta:
        model = Login
        fields = ['id', 'nome', 'senha']