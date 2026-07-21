from rest_framework import viewsets
from ..models import NycCensusBlock
from ..serializers import NycCensusBlockSerializer


class NycCensusBlockViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NycCensusBlock.objects.all()
    serializer_class = NycCensusBlockSerializer