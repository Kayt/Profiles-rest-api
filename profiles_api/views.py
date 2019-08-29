from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework import viewsets

from profiles_api import serializers
from profiles_api import models


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSetializer
    queryset = models.UserProfile.objects.all()