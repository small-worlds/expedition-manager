from rest_framework import viewsets, mixins
from django.contrib.auth.models import User
from accounts.models import Profile
from accounts.serializers import ProfileSerializer, UserSerializer
from accounts.permissions import IsStaffOrTargetUser


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
