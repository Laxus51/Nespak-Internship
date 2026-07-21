from rest_framework import serializers
from ..models import NycHomicide

class NycHomicideSerializer(serializers.ModelSerializer):
    class Meta:
        model = NycHomicide
        fields = "__all__"