from rest_framework import viewsets, mixins
from django.contrib.auth.models import User
from accounts.serializers import UserSerializer, ProfileSerializer
from accounts.permissions import IsStaffOrTargetUser, IsUserOrReadOnly
from accounts.models import Profile

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update`, and `destroy` actions. `list` will only list active users.
    All other actions are valid only for the authenticated user.
    """
    queryset = User.objects.filter(is_active=True)
    model = User
    serializer_class = UserSerializer
    permission_classes = [IsStaffOrTargetUser]


class ProfileViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin):
    """
    TODO: Define list
    """
    queryset = Profile.objects.all()
    model = Profile
    serializer_class = ProfileSerializer
    permissions_classes = [IsUserOrReadOnly]
