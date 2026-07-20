from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NycSubwayStationViewSet

router = DefaultRouter()
router.register(r"stations", NycSubwayStationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]