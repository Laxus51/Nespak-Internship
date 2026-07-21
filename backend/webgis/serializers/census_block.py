from rest_framework import serializers
from ..models import NycCensusBlock

class NycCensusBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = NycCensusBlock
        fields = "__all__"