from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from api.permissions import IsOwnerOrReadOnly
from api.models import BelStop
from api.serializers import UserSerializer
from api.serializers import BelStopSerializer

# Create your views here.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Viewset for list and detail of user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BelStopViewSet(viewsets.ModelViewSet):
    queryset = BelStop.objects.all()
    serializer_class = BelStopSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
