from rest_framework import serializers
from expeditions.models import Expedition, Waypoint


class ExpeditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expedition
        fields = ('id', 'created', 'name', 'start_date', 'end_date', 'min_jump')

class WaypointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waypoint
        fields = ('id', 'created', 'system', 'planet', 'expedition', 'number')
