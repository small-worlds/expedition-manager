from rest_framework import viewsets, generics, mixins
import expeditions.serializers
from expeditions.models import Expedition, Waypoint, Registration
from expeditions.permissions import IsAdminOrReadOnly, IsRegistrantOrReadOnly, IsRegistrant


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
    serializer_class = expeditions.serializers.RegistrationSerializer
    permission_classes = [IsRegistrantOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Registration.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = Registration.objects.filter(user=user)
        return queryset


class ExpeditionRegistrationList(generics.ListAPIView):
    """
    List all registrations for a given expedition
    """
    serializer_class = expeditions.serializers.RegistrationSerializer

    def get_queryset(self):
        expedition = self.kwargs['pk']
        return Registration.objects.filter(expedition=expedition)


class RegistrationSelfViewSet(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    """
    List all registrations for yourself
    """
    serializer_class = expeditions.serializers.RegistrationSerializer
    permission_classes = [IsRegistrant]

    def get_queryset(self):
        return Registration.objects.filter(user=self.request.user)
