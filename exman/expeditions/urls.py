from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from expeditions import views


router = DefaultRouter()
router.register(r'expeditions', views.ExpeditionViewSet)
router.register(r'waypoints', views.WaypointViewSet)

urlpatterns = [
    url('^', include(router.urls)),
]
