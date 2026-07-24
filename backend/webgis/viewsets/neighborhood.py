from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models import NycNeighborhood, NycSubwayStation, NycStreet, NycHomicide, NycCensusBlock
from ..serializers import NycNeighborhoodSerializer, NycSubwayStationSerializer, NycNeighborhoodDetailSerializer

class NycNeighborhoodViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NycNeighborhood.objects.all()
    serializer_class = NycNeighborhoodSerializer

    @action(detail=True, methods=["get"])
    def subway_stations(self, request, pk=None):
        neighborhood = self.get_object()
        subway_stations = NycSubwayStation.objects.filter(geom__within=neighborhood.geom)
        serializer = NycSubwayStationSerializer(subway_stations, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=["get"])
    def details(self, request, pk=None):
        neighborhood = self.get_object()
        subway_stations = NycSubwayStation.objects.filter(geom__within=neighborhood.geom)
        streets = NycStreet.objects.filter(geom__intersects=neighborhood.geom)
        homicides = NycHomicide.objects.filter(geom__within=neighborhood.geom)
        census_blocks = NycCensusBlock.objects.filter(geom__intersects=neighborhood.geom)

        serializer = NycNeighborhoodDetailSerializer({
            "neighborhood": neighborhood,
            "subway_stations": subway_stations,
            "streets": streets,
            "homicides": homicides,
            "census_blocks": census_blocks
        })

        return Response(serializer.data)
        