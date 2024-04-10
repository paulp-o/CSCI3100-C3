from rest_framework import serializers
from .models import UserData


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        # Add or remove fields as needed.
        fields = ['id', 'settings', 'customization',
                  'purchased_items', 'highscores', 'profile', 'money']
