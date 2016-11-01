from rest_framework import serializers
from expeditions.models import Expedition, Waypoint, Registration


class ExpeditionSerializer(serializers.ModelSerializer):
    waypoints = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='waypoint-detail')
    # registrations = serializers.HyperlinkedIdentityField(view_name='expeditionregistration-list')
    class Meta:
        model = Expedition
        fields = '__all__'


class WaypointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waypoint
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
        read_only_fields = ('registration_number',)
