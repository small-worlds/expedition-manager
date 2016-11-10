from rest_framework import viewsets, generics, mixins
from api.serializers import *
from api.permissions import *
from rest_framework.permissions import IsAuthenticated
from expeditions.models import Expedition, Waypoint, Registration


class ProfileViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
    `list`, `retrieve`, and `update` actions. Only staff or the target user can modify a profile.
    """
    queryset = Profile.objects.all()
    model = Profile
    serializer_class = ProfileSerializer
    permission_classes = [IsStaffOrTargetUser, ]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    `list` and `retrieve` actions.
    """
    queryset = User.objects.filter(is_active=True)
    model = User
    serializer_class = UserSerializer


class ExpeditionViewSet(viewsets.ModelViewSet):
    """
    List all expeditions, or create a new expedition.
    """
    queryset = Expedition.objects.filter(published=True)
    serializer_class = ExpeditionSerializer
    permission_classes = [IsAdminOrReadOnly]


class WaypointViewSet(viewsets.ModelViewSet):
    """
    List all waypoints, or create a new waypoint.
    """
    queryset = Waypoint.objects.all()
    serializer_class = WaypointSerializer
    permission_classes = [IsAdminOrReadOnly]


class RegistrationViewSet(viewsets.ModelViewSet):
    """
    List all registrations, or create a new registration.
    """
    serializer_class = RegistrationSerializer
    permission_classes = [IsRegistrantOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Registration.objects.all()
        user = self.request.query_params.get('user', None)
        expedition = self.request.query_params.get('expedition', None)
        if user is not None:
            if expedition is not None:
                queryset = Registration.objects.filter(user=user, expedition=expedition)
            else:
                queryset = Registration.objects.filter(user=user)
        elif expedition is not None:
            queryset = Registration.objects.filter(expedition=expedition)
        return queryset


class ExpeditionRegistrationList(generics.ListAPIView):
    """
    List all registrations for a given expedition
    """
    serializer_class = RegistrationSerializer

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
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated, IsRegistrant]

    def get_queryset(self):
        return Registration.objects.filter(user=self.request.user)
