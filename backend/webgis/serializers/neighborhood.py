from rest_framework import serializers
from ..models import NycNeighborhood

class NycNeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = NycNeighborhood
        fields = "__all__"