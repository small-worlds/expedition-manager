from rest_framework import viewsets
from django.contrib.auth.models import User
from accounts.serializers import UserSerializer
from accounts.permissions import IsStaffOrTargetUser


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update`, and `destroy` actions. `list` will only list active users.
    All other actions are valid only for the authenticated user.
    """
    queryset = User.objects.filter(is_active=True)
    model = User
    serializer_class = UserSerializer
    permission_classes = [IsStaffOrTargetUser,]
