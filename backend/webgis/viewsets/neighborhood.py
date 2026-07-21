from rest_framework import viewsets
from ..models import NycNeighborhood
from ..serializers import NycNeighborhoodSerializer

class NycNeighborhoodViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NycNeighborhood.objects.all()
    serializer_class = NycNeighborhoodSerializer