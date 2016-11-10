from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api import views



router = DefaultRouter()

router.register(r'profiles', views.ProfileViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'expeditions', views.ExpeditionViewSet)
router.register(r'waypoints', views.WaypointViewSet)
router.register(r'registrations', views.RegistrationViewSet, base_name='registration')
router.register(r'my-registrations', views.RegistrationSelfViewSet, base_name='my-registration')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^expeditions/(?P<pk>[0-9]+)/registrations/', views.ExpeditionRegistrationList.as_view())
]