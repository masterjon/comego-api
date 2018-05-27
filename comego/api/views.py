from rest_framework.viewsets import ModelViewSet
from . import serializers, models


class CategoryItemViewSet(ModelViewSet):
    queryset = models.CategoryItem.objects.all()
    serializer_class = serializers.CategoryItemSerializer


class CategoryNestedItemViewSet(ModelViewSet):
    queryset = models.CategoryItem.objects.all()
    serializer_class = serializers.CategoryNestedItemSerializer


class BoletinViewSet(ModelViewSet):
    queryset = models.Boletin.objects.all()
    serializer_class = serializers.BoletinSerializer


class GuiaViewSet(ModelViewSet):
    queryset = models.Guia.objects.all()
    serializer_class = serializers.GuiaSerializer


class PodcastViewSet(ModelViewSet):
    queryset = models.Podcast.objects.all()
    serializer_class = serializers.PodcastSerializer


class LeyViewSet(ModelViewSet):
    queryset = models.Ley.objects.all()
    serializer_class = serializers.LeySerializer


class NormaViewSet(ModelViewSet):
    queryset = models.Norma.objects.all()
    serializer_class = serializers.NormaSerializer


class ReglamentoViewSet(ModelViewSet):
    queryset = models.Reglamento.objects.all()
    serializer_class = serializers.ReglamentoSerializer
