from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class ECGTests(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='user',
            email='user@mail.com',
            password='secret_password',
        )
        self.token = Token.objects.create(user=self.user)

    def test_home(self):
        """
        Ensure we can access home page with a token.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        home_path = reverse('ecg-handler:home')
        request = self.client.get(home_path, format='json')
        self.assertEqual(request.status_code, 200)
