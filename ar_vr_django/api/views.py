from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User

from polls.models import Polls
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class PollsViewSet(viewsets.ModelViewSet):
	queryset = Polls.objects.all()
	serializer_class = PollsSerializer