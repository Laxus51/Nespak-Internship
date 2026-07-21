from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import NycSubwayStationViewSet, NycStreetViewSet, NycNeighborhoodViewSet, NycHomicideViewSet, NycCensusBlockViewSet

router = DefaultRouter()
router.register(r"stations", NycSubwayStationViewSet)
router.register(r"neighborhoods", NycNeighborhoodViewSet)
router.register(r"streets", NycStreetViewSet)
router.register(r"homicides", NycHomicideViewSet)
router.register(r"census-blocks", NycCensusBlockViewSet)

urlpatterns = [
    path("", include(router.urls)),
]