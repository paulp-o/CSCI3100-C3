from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    settings = models.JSONField(default=dict)
    customization = models.JSONField(default=dict)
    purchased_items = models.JSONField(default=dict)
    highscores = models.JSONField(default=dict)
    profile = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
