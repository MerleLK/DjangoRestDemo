"""
    This views is refer the restful style
"""
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
        show and edit the user view.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
        show and edit the group view.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer