from rest_framework import serializers
from api.models import BelStop, BelMeeting
from django.contrib.auth.models import User


class BelStopSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = BelStop
        fields = ('url', 'pk', 'owner', 'location',
            'spots_available','times_available', 'accepts_belPoints')

class BelMeetingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BelMeeting
        fields = ('belStop', 'datetime', 'topic', 'category')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    belstops = serializers.HyperlinkedRelatedField(many=True, view_name='belstop-detail', read_only=True)
    #bel_meetings  = serializers.HyperlinkedRelatedField(many=True, view_name='belmeeting-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'pk', 'username', 'belstops')
