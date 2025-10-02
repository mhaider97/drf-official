from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Snippet

class SnippetTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.snippet = Snippet.objects.create(
            owner=self.user,
            title='Test Snippet',
            code='print("Hello, world!")',
            language='python'
        )

    def test_create_snippet(self):
        """
        Ensure we can create a new snippet object.
        """
        self.client.login(username='testuser', password='testpassword')
        url = '/snippets/'
        data = {'title': 'New Snippet', 'code': 'print("New world!")', 'language': 'python'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Snippet.objects.count(), 2)
        self.assertEqual(Snippet.objects.get(id=2).title, 'New Snippet')

    def test_get_snippets(self):
        """
        Ensure we can retrieve a list of snippets.
        """
        url = '/snippets/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_snippet_detail(self):
        """
        Ensure we can retrieve a single snippet.
        """
        url = f'/snippets/{self.snippet.id}/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.snippet.title)

    def test_update_snippet(self):
        """
        Ensure we can update a snippet.
        """
        self.client.login(username='testuser', password='testpassword')
        url = f'/snippets/{self.snippet.id}/'
        data = {'title': 'Updated Snippet', 'code': 'print("Updated world!")', 'language': 'python'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.snippet.refresh_from_db()
        self.assertEqual(self.snippet.title, 'Updated Snippet')

    def test_delete_snippet(self):
        """
        Ensure we can delete a snippet.
        """
        self.client.login(username='testuser', password='testpassword')
        url = f'/snippets/{self.snippet.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Snippet.objects.count(), 0)

    def test_unauthenticated_user_cannot_create_snippet(self):
        """
        Ensure unauthenticated users cannot create snippets.
        """
        url = '/snippets/'
        data = {'title': 'New Snippet', 'code': 'print("New world!")', 'language': 'python'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_get_users(self):
        """
        Ensure we can retrieve a list of users.
        """
        url = '/users/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_user_detail(self):
        """
        Ensure we can retrieve a single user.
        """
        url = f'/users/{self.user.id}/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)
