from rest_framework.viewsets import ModelViewSet
# from rest_framework.generics import ListAPIView
# from django.db.models import Count

from . import serializers, models


# class ActivityDatesViewSet(ListAPIView):
#     serializer_class = serializers.ActividadSerializer

#     def get_queryset(self):
#         return models.Actividad.objects.values("month").annotate(count=Count("month"))
class ActivityViewSet(ModelViewSet):
    queryset = models.Actividad.objects.all()
    serializer_class = serializers.ActividadSerializer


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


class SponsorViewSet(ModelViewSet):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializers.SponsorSerializer
