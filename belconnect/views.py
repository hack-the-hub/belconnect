from django.shortcuts import render
from rest_framework import serializers, viewsets

from belconnect.serializers import BelStopSerializer
from api.models import BelStop


# Create your views here.

# View Sets

class BelStopViewSet(viewsets.ModelViewSet):
    queryset = BelStop.objects.all()
    serializer_class = BelStopSerializer


#class BelMeetingViewSet(viewsets.ModelViewSet):
#    queryset = BelMeeting.objects.all()
#    serializer_class = BelMeetingSerializer
