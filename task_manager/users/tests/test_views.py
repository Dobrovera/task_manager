from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):

        self.client = Client()
        self.users_url = reverse('users')
        self.create_url = reverse('create')
        User.objects.create(
            username='test_1',
            password='test_1',
            first_name='test_1',
            last_name='test_1',
        )
        User.objects.create(
            username='test_2',
            password='test_2',
            first_name='test_2',
            last_name='test_2',
        )

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
        self.assertTrue(User.objects.filter(username="TestUser"))
        self.assertTrue(User.objects.filter(first_name="Test"))

    def test_LoginView_GET(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='login.html')

    def test_UserUpdateView_GET(self):
        user = User.objects.get(username='test_1')
        response = self.client.get(reverse('update', kwargs={'id': user.id}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users'))
        self.client.force_login(user)
        response = self.client.get(reverse('update', kwargs={'id': user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='users/update.html')

    def test_UserUpdateView_POST(self):
        user = User.objects.get(username='test_2')
        self.client.force_login(user)
        response = self.client.post(
            reverse('update', kwargs={'id': user.id}),
            {
                'username': 'test_update',
                'first_name': 'test_update',
                'last_name': 'test_update',
                'password1': 'test_update',
                'password2': 'test_update',
            }
        )
        self.assertEqual(response.status_code, 302)
        user.refresh_from_db()
        self.assertEqual(user.username, 'test_update')
        self.assertEqual(user.username, 'test_update')
        self.assertRedirects(response, reverse('users'))
