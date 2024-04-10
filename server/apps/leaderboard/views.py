from rest_framework import views, status, response
from .models import Player
from .serializers import PlayerSerializer
#from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UpdateDataView(views.APIView):
#   permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = []
    permission_classes = [] 

    def post(self, request):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveDataView(views.APIView):
    permission_classes = []

    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)