from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APIClient


class TaskTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_should_list_all_tasks(self):
        url = reverse('tasks-list')
        response: Response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) == 0)


class HelloTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_hello(self):
        url = reverse('hello')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ping_pong(self):
        data = {'name': 'Ely'}
        url = reverse('ping_pong')

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('pong' in response.data)
        self.assertEqual(response.data['pong'], 'Ely')
