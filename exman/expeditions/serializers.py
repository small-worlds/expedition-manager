from rest_framework import serializers
from expeditions.models import Expedition, Waypoint, Registration


class ExpeditionSerializer(serializers.ModelSerializer):
    waypoints = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='waypoint-detail')
    registrations = serializers.HyperlinkedIdentityField(view_name='expedition-registration-list')
    class Meta:
        model = Expedition
        fields = ('id', 'created', 'name', 'start_date', 'end_date', 'min_jump', 'waypoints', 'registrations')


class WaypointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waypoint
        fields = ('id', 'created', 'system', 'planet', 'expedition', 'number')


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ('id', 'created', 'updated', 'name', 'email', 'region', 'ship_model', 'ship_name', 'ship_jump',
                  'expedition')
