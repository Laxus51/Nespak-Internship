from rest_framework import viewsets
from .models_existing import NycSubwayStation
from .serializers import NycSubwayStationSerializer


class NycSubwayStationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NycSubwayStation.objects.all()
    serializer_class = NycSubwayStationSerializer