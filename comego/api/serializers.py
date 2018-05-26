from rest_framework.serializers import ModelSerializer, ReadOnlyField
from . import models


class ActividadSerializer(ModelSerializer):
    salon = ReadOnlyField(source='salon.title')

    class Meta:
        model = models.Actividad
        fields = '__all__'


class ActivityCategorySerializer(ModelSerializer):
    actividades = ActividadSerializer(many=True)

    class Meta:
        model = models.ActivityCategory
        fields = '__all__'


class CategoryItemSerializer(ModelSerializer):

    activity_category = ActivityCategorySerializer(many=True)

    class Meta:
        model = models.CategoryItem
        fields = '__all__'


class BoletinSerializer(ModelSerializer):
    class Meta:
        model = models.Boletin
        fields = '__all__'


class GuiaSerializer(ModelSerializer):
    class Meta:
        model = models.Guia
        fields = '__all__'


class PartsSerializers(ModelSerializer):
    class Meta:
        model = models.UrlItem
        fields = '__all__'


class PodcastSerializer(ModelSerializer):
    parts = PartsSerializers(many=True)

    class Meta:
        model = models.Podcast
        fields = ('__all__')


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
