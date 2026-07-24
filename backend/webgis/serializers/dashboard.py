from rest_framework import serializers

class TopNeighborhoodSerializer(serializers.Serializer):
    name = serializers.CharField()
    station_count = serializers.IntegerField()