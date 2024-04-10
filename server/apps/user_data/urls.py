from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserDataViewSet

router = DefaultRouter()
router.register(r'get_by_id', UserDataViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('update/', UserDataViewSet.as_view({'patch': 'partial_update'})),
]
