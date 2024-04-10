from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class UserDataTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='pass')
        self.admin = User.objects.create_superuser(
            username='admin', password='admin')
        self.client = APIClient()

    def test_read_user_data_unauthenticated(self):
        # Adjust the URL name based on your router configuration
        response = self.client.get(reverse('user_data:users-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_user_data_as_owner(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(reverse(
            'user_data:users-detail', args=[self.user.userdata.id]), {'settings': 'new settings'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['settings'], 'new settings')

    def test_edit_user_data_as_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.patch(reverse(
            'user_data:users-detail', args=[self.user.userdata.id]), {'settings': 'admin settings'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['settings'], 'admin settings')

    def test_edit_user_data_unauthenticated(self):
        response = self.client.patch(reverse(
            'user_data:users-detail', args=[self.user.userdata.id]), {'settings': 'unauthorized settings'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
