from rest_framework import viewsets
from .models import UserData
from .serializers import UserDataSerializer
from .permissions import IsOwnerOrAdminOrReadOnly


class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]

    def get_queryset(self):
        """
        Optionally restricts the returned data to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = super().get_queryset()
        username = self.request.query_params.get('username')
        if username is not None:
            queryset = queryset.filter(user__username=username)
        return queryset
