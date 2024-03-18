from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from api.filters import UserFilter
from api.models import User
from api.decorator import route_permissions
from api.serializers import UserSerializer


class UserListViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.exclude(role__code_name='su').filter(profile_status='Current').order_by('appointment_order')
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter

    @route_permissions(['read_user'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
