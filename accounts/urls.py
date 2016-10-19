from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from accounts import views


router = SimpleRouter()
router.register(r'users', views.UserViewSet)
router.register(r'usersadmin', views.UserAdminViewSet)

urlpatterns = [
    url('^', include(router.urls)),
]
