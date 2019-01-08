from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from . import models


class ElectrocardiogramTests(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='user',
            email='user@mail.com',
            password='secret_password'
        )
        self.token = Token.objects.create(user=self.user)

    def tearDown(self):
        try:
            electrocardiogram = models.Electrocardiogram.objects.get(first_name='Testname',
                                                                     last_name='Testsurname')
            electrocardiogram.delete()
        except models.Electrocardiogram.DoesNotExist:
            pass

    def test_create_successful(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        create_path = reverse('ecg-handler:electrocardiogram-create')
        data = {
            'first_name': 'Testname',
            'last_name': 'Testsurname'
        }
        request = self.client.post(create_path, format='json', data=data)
        self.assertEqual(request.status_code, 201)

    def test_create_error(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        create_path = reverse('ecg-handler:electrocardiogram-create')
        data = {
            'first_name': 'Name',
            'last_name': None
        }
        request = self.client.post(create_path, format='json', data=data)
        self.assertEqual(request.status_code, 400)


class SignalTests(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='user',
            email='user@mail.com',
            password='secret_password'
        )
        self.token = Token.objects.create(user=self.user)
        self.electrocardiogram = models.Electrocardiogram(
            first_name='Testname',
            last_name='Testsurname'
        ).save()

    def tearDown(self):
        self.electrocardiogram.signals.clear()
        self.electrocardiogram.save()
        self.electrocardiogram.delete()

    def test_create_start(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        create_path = reverse('ecg-handler:signal-create')
        data = {
            'electrocardiogram_id': str(self.electrocardiogram.id),
            'signals': [1, 2, 3, 4, 5],
        }
        request = self.client.post(create_path, format='json', data=data)
        self.assertEqual(request.status_code, 201)

    def test_create_end(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        create_path = reverse('ecg-handler:signal-create')
        data = {
            'electrocardiogram_id': str(self.electrocardiogram.id),
            'signals': [6, 7, 8, 9, 10],
            'last_portion': True,
        }
        request = self.client.post(create_path, format='json', data=data)
        self.assertEqual(request.status_code, 201)

    def test_create_end_error(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        create_path = reverse('ecg-handler:signal-create')
        data = {
            'electrocardiogram_id': str(self.electrocardiogram.id),
            'signals': [1, 2, 3, 4, 5],
            'last_portion': True,
        }
        self.client.post(create_path, format='json', data=data)

        data = {
            'electrocardiogram_id': str(self.electrocardiogram.id),
            'signals': [6, 7, 8, 9, 10],
        }
        request = self.client.post(create_path, format='json', data=data)
        self.assertEqual(request.status_code, 400)

    def test_create_invalid_id(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        create_path = reverse('ecg-handler:signal-create')
        data = {
            'electrocardiogram_id': str(self.electrocardiogram.id) + 'a',
            'signals': [1, 2, 3, 4, 5],
        }
        request = self.client.post(create_path, format='json', data=data)
        self.assertEqual(request.status_code, 400)

    def test_create_not_number_signals(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        create_path = reverse('ecg-handler:signal-create')
        data = {
            'electrocardiogram_id': str(self.electrocardiogram.id),
            'signals': ['a', 'b', 'c', 4, 5],
        }
        request = self.client.post(create_path, format='json', data=data)
        self.assertEqual(request.status_code, 400)
