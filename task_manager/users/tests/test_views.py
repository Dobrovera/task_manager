from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):

        self.client = Client()
        self.users_url = reverse('users')
        self.create_url = reverse('create')

    def test_UserListView_GET(self):
        response = self.client.get(self.users_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users.html')

    def test_SignUpView_GET(self):
        response = self.client.get(self.create_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/create.html')

    def test_SignUpView_POST(self):
        response = self.client.post(
            '/users/create/',
            {
                'first_name': 'Test',
                'last_name': 'Test',
                'username': 'TestUser',
                'password1': '12345678',
                'password2': '12345678',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="Test"))
