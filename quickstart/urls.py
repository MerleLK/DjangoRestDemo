"""
    This is part urls from quick start
"""
from rest_framework import routers
from quickstart.views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)