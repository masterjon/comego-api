from rest_framework.serializers import ModelSerializer
from .models import Boletin


class BoletinSerializer(ModelSerializer):
    class Meta:
        model = Boletin
        fields = '__all__'
