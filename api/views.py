from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from api.permissions import IsOwnerOrReadOnly
from api.models import BelStop
from api.serializers import UserSerializer
# Create your views here.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Viewset for list and detail of user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
