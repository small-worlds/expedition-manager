from rest_framework import viewsets, generics
import expeditions.serializers
from expeditions.models import Expedition, Waypoint, Registration
from expeditions.permissions import IsAdminOrReadOnly, IsRegistrantOrReadOnly


class ExpeditionViewSet(viewsets.ModelViewSet):
    """
    List all expeditions, or create a new expedition.
    """
    queryset = Expedition.objects.all()
    serializer_class = expeditions.serializers.ExpeditionSerializer
    permission_classes = [IsAdminOrReadOnly]


class WaypointViewSet(viewsets.ModelViewSet):
    """
    List all waypoints, or create a new waypoint.
    """
    queryset = Waypoint.objects.all()
    serializer_class = expeditions.serializers.WaypointSerializer
    permission_classes = [IsAdminOrReadOnly]


class RegistrationViewSet(viewsets.ModelViewSet):
    """
    List all registrations, or create a new registration.
    """
    queryset = Registration.objects.all()
    serializer_class = expeditions.serializers.RegistrationSerializer
    permission_classes = [IsRegistrantOrReadOnly]

class ExpeditionRegistrationList(generics.ListAPIView):
    """
    List all registrations for a given expedition
    """
    serializer_class = expeditions.serializers.RegistrationSerializer

    def get_queryset(self):
        expedition = self.kwargs['pk']
        return Registration.objects.filter(expedition=expedition)
