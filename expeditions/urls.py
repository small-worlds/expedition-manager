from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from expeditions import views


router = DefaultRouter()
router.register(r'expeditions', views.ExpeditionViewSet)
router.register(r'waypoints', views.WaypointViewSet)
router.register(r'registrations', views.RegistrationViewSet)

urlpatterns = [
    url('^', include(router.urls)),
    url(r'^expedition-registrations/(?P<pk>.+)/$', views.ExpeditionRegistrationList.as_view(), name='expedition-registration-list')
]
