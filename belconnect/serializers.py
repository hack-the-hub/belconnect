from api import models
from rest_framework import serializers

class BelStopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.BelStop
        fields = ('location', 'spots_available', 'times_available',
                  'accepts_belPoints')

#class BelMeetingSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = models.BelMeeting
#        fields = ('belStop', 'datetime', 'days_available', 'times_available',
#                  'accepts_belPoints')