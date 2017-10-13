from rest_framework.routers import DefaultRouter

from simpleDemo import views

simple_router = DefaultRouter()
simple_router.register(
    r'simple',
    views.AccountViewSet,
)
