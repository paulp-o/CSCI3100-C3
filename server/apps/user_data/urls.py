from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserDataViewSet

router = DefaultRouter()
router.register(r'users', UserDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
