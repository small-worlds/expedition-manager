from rest_framework import viewsets
from rest_framework.decorators import detail_route
from expeditions.models import Expedition, Waypoint
from expeditions.serializers import ExpeditionSerializer, WaypointSerializer


class ExpeditionViewSet(viewsets.ModelViewSet):
    """
    List all expeditions, or create a new expedition.
    """
    queryset = Expedition.objects.all()
    serializer_class = ExpeditionSerializer


class WaypointViewSet(viewsets.ModelViewSet):
    """
    List all waypoints, or create a new waypoint.
    """
    queryset = Waypoint.objects.all()
    serializer_class = WaypointSerializer