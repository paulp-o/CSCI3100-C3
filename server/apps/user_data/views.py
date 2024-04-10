from rest_framework import viewsets, status, response
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import UserData
from .serializers import UserDataSerializer
from .permissions import IsOwnerOrAdminOrReadOnly


class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]

    def get_queryset(self):
        """
        requires id parameter in url.
        responds with all user information within the userdata database
        """
        queryset = UserData.objects.all()
        id = self.request.query_params.get('id', None)
        if id is None:  # if no id, error
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
        return queryset.filter(id=id)

    def partial_update(self, request, *args, **kwargs):
        """
        requires id parameter in url, and data in request body, and token in header
        responds with applied changes
        """
        user = request.user
        instance = UserData.objects.get(user=user)
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
