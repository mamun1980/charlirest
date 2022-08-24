from django.test import TestCase
from django.urls import reverse
from rest_framework import status
# from django.contrib.auth.models import User
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIRequestFactory
from .models import *
from .views import *

class HelloWorldTestCase(APITestCase):

    def test_hello_world(self):
        response = self.client.get('/users/')

        # print(User.objects.count())
        # # print(response['context_data'])
        # # print(response['context'])
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data[0]['username'], 'admin')
        # self.assertEqual(User.objects.count(), 2)
        # self.assertEqual(User.objects.first().username, 'admin')

class PostTests(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        return super().setUp()

    def test_create_post(self):
        """
        Ensure we can create a new account object.
        """
        # url = reverse('posts')
        # data = {'name': 'DabApps'}
        # response = self.client.post(url, data, format='json')

        
        request = factory.post('/posts/', {'title': 'title 1', "content": "content 1"}, format='json')

        response = PostViewSet.as_view(request)
        print(dir(response))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# Create your tests here.
