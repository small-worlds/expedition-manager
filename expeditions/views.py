from rest_framework import viewsets, generics
from expeditions.models import Expedition, Waypoint, Registration
from expeditions.serializers import ExpeditionSerializer, WaypointSerializer, RegistrationSerializer


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


class RegistrationViewSet(viewsets.ModelViewSet):
    """
    List all registrations, or create a new registration.
    """
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class ExpeditionRegistrationList(generics.ListAPIView):
    """
    List all registrations for a given expedition
    """
    serializer_class = RegistrationSerializer

    def get_queryset(self):
        expedition = self.kwargs['pk']
        return Registration.objects.filter(expedition=expedition)
