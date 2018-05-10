from rest_framework.serializers import ModelSerializer
from . import models


class BoletinSerializer(ModelSerializer):
    class Meta:
        model = models.Boletin
        fields = '__all__'


class GuiaSerializer(ModelSerializer):
    class Meta:
        model = models.Guia
        fields = '__all__'


class PodcastSerializer(ModelSerializer):
    class Meta:
        model = models.Podcast
        fields = '__all__'


class LeySerializer(ModelSerializer):
    class Meta:
        model = models.Ley
        fields = '__all__'


class NormaSerializer(ModelSerializer):
    class Meta:
        model = models.Norma
        fields = '__all__'


class ReglamentoSerializer(ModelSerializer):
    class Meta:
        model = models.Reglamento
        fields = '__all__'
