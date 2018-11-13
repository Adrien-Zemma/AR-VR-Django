from rest_framework import serializers
from django.contrib.auth.models import User
from polls.models import Polls

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class PollsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Polls
		fields = '__all__'