# Create your models here.

# Model for the Leaderboard, typically linked to the User and/or GameSession models.
# Stores the high scores and possibly references to the corresponding game sessions.
from django.db import models

class Player(models.Model):
    player_id = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return self.player_id