from rest_framework import viewsets 
from ..models import NycHomicide
from ..serializers import NycHomicideSerializer

class NycHomicideViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NycHomicide.objects.all()
    serializer_class = NycHomicideSerializer