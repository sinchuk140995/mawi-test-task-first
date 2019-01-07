from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class ElectrocardiogramTests(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='user',
            email='user@mail.com',
            password='secret_password',
        )
        self.token = Token.objects.create(user=self.user)

    def test_create_successful(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        create_path = reverse('ecg-handler:electrocardiogram-create')
        data = {
            'first_name': 'Name',
            'last_name': 'Surame',
        }
        request = self.client.post(create_path, format='json', data=data)
        self.assertEqual(request.status_code, 201)

    def test_create_error(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        create_path = reverse('ecg-handler:electrocardiogram-create')
        data = {
            'first_name': 'Name',
            'last_name': None,
        }
        request = self.client.post(create_path, format='json', data=data)
        self.assertEqual(request.status_code, 400)
