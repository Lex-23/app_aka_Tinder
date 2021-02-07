from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet
from users.views import UserViewSet


router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"users", UserViewSet)


urlpatterns = [path("", include(router.urls))]
