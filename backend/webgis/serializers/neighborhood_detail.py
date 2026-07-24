from rest_framework import serializers
from ..serializers import (
    NycSubwayStationSerializer, 
    NycStreetSerializer, 
    NycHomicideSerializer, 
    NycCensusBlockSerializer, 
    NycNeighborhoodSerializer
)

class NycNeighborhoodDetailSerializer(serializers.Serializer):
    neighborhood = NycNeighborhoodSerializer()
    subway_stations = NycSubwayStationSerializer(many=True)
    streets = NycStreetSerializer(many=True)
    homicides = NycHomicideSerializer(many=True)
    census_blocks = NycCensusBlockSerializer(many=True)
