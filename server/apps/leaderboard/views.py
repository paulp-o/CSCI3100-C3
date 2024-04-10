from django.shortcuts import render

# Create your views here.

# Views for retrieving the leaderboard data.
# Endpoints for fetching and possibly updating leaderboard entries.

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status, views, permissions, response
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer


class LeaderboardView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def update_ranking(self, user, ranking):
        # Assuming you have a 'Leaderboard' model with fields 'user' and 'ranking'
        # Update the user's ranking in the database
        leaderboard = Leaderboard.objects.get(user=user)
        leaderboard.ranking = ranking
        leaderboard.save()

    def update_score(self, user, score):
        # Assuming you have a 'Leaderboard' model with fields 'user' and 'ranking'
        # Update the user's ranking in the database
        leaderboard = Leaderboard.objects.get(user=user)
        leaderboard.score = score
        leaderboard.save()

    def retrieve_ranking_score(self, user):
        # Assuming you have a 'Leaderboard' model with fields 'user' and 'ranking'
        # Retrieve the user's ranking from the database
        leaderboard = Leaderboard.objects.get(user=user)
        return leaderboard.ranking, leaderboard.score

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            ranking = request.data.get('ranking')
            score = request.data.get('score')
            self.update_ranking(user, ranking)
            self.update_score(user, score)
            return response.Response({'token': token.key}, status=status.HTTP_200_OK)
        
        return response.Response(status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        # Retrieve the leaderboard ranking for the authenticated user
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            ranking, score = self.retrieve_ranking_score(user)
            return response.Response({'ranking': ranking, 'score': score}, status=status.HTTP_200_OK)
        
        return response.Response(status=status.HTTP_401_UNAUTHORIZED)