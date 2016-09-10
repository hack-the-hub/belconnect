from rest_framework import serializers
from api.models import BelStop
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    bel_stops = serializers.HyperlinkedRelatedField(many=True, view_name='belstop-detail', read_only=True)
    #bel_meetings  = serializers.HyperlinkedRelatedField(many=True, view_name='belmeeting-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'pk', 'username', 'bel_stops')

class BelStopSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = BelStop
        fields = ('url', 'pk', 'owner', 'location',
            'spots_available','times_available', 'accepts_belPoints')
