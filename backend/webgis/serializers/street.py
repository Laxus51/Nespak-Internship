from rest_framework import serializers
from ..models import NycStreet

class NycStreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = NycStreet
        fields = "__all__"