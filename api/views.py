from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from api.permissions import IsOwnerOrReadOnly
from api.models import BelStop, BelMeeting, CATEGORIES
from api.serializers import UserSerializer
from api.serializers import BelStopSerializer, BelMeetingSerializer
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model


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


class BelMeetingViewSet(viewsets.ModelViewSet):
    queryset = BelMeeting.objects.all()
    serializer_class = BelMeetingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CreateUserView(CreateAPIView):
    model = get_user_model()
    # set the permissions from the class
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

def getAllCategories(request):
    return HttpResponse(CATEGORIES)