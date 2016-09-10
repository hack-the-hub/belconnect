from rest_framework import serializers
from api.models import BelStop
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class BelStopSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = BelStop
        fields = ('url', 'pk', 'owner', 'location',
            'spots_available','times_available', 'accepts_belPoints')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    belstops = serializers.HyperlinkedRelatedField(many=True, view_name='belstop-detail', read_only=True)
    #bel_meetings  = serializers.HyperlinkedRelatedField(many=True, view_name='belmeeting-detail', read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('url', 'pk', 'username','password', 'belstops')


    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username']
        )

        # set the password
        user.set_password(validated_data['password'])
        user.save()
        return user
