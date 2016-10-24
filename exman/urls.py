"""exman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
import accounts.views as account_views
import expeditions.views as expedition_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', account_views.UserViewSet)
router.register(r'expeditions', expedition_views.ExpeditionViewSet)
router.register(r'waypoints', expedition_views.WaypointViewSet)
router.register(r'registrations', expedition_views.RegistrationViewSet)

urlpatterns = [
    url('^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
