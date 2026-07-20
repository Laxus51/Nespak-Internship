from rest_framework import serializers
from .models_existing import NycSubwayStation


class NycSubwayStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NycSubwayStation
        fields = "__all__"