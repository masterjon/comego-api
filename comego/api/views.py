from rest_framework.viewsets import ModelViewSet
from .serializers import BoletinSerializer
from .models import Boletin


class BoletinViewSet(ModelViewSet):
    queryset = Boletin.objects.all()
    serializer_class = BoletinSerializer
