from django.urls import path
from .views import UpdateDataView, RetrieveDataView

urlpatterns = [
    path('update/', UpdateDataView.as_view(), name='update_data'),
    path('retrieve/', RetrieveDataView.as_view(), name='retrieve_data'),
]