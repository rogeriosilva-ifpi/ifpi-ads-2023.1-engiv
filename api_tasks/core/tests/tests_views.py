from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class SignupTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_should_create_user(self):
        data = {
            'username': 'rogerio410',
            'email': 'rogerio410@gmail.com',
            'password': '123456'
        }
        url = reverse('signup')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 201)

    def test_should_not_create_user_with_short_pass(self):
        data = {
            'username': 'rogerio410',
            'email': 'rogerio410@gmail.com',
            'password': '1234'
        }
        url = reverse('signup')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIs('curta' in response.data['password'][0], True)
