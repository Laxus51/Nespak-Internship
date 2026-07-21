from rest_framework import viewsets
from ..models import NycStreet
from ..serializers import NycStreetSerializer

class NycStreetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NycStreet.objects.all()
    serializer_class = NycStreetSerializer