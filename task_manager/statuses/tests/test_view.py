from django.contrib.auth.models import User
from task_manager.statuses.models import Status
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):

        self.client = Client()
        self.create_status = reverse('create_status')
        self.statuses = reverse('statuses')
        Status.objects.create(
            id=1,
            name='test_status'
        )
        User.objects.create(
            username='test_5',
            password='test_5',
            first_name='test_5',
            last_name='test_5',
        )

    def test_StatusesListView_GET(self):
        response = self.client.get(self.statuses)
        self.assertEquals(response.status_code, 302)

        user = User.objects.get(username='test_5')
        self.client.force_login(user)
        response = self.client.get(self.statuses)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/statuses.html')

    def test_StatusCreateView_GET(self):
        response = self.client.get(self.create_status)
        self.assertEquals(response.status_code, 302)

        user = User.objects.get(username='test_5')
        self.client.force_login(user)
        response = self.client.get(self.create_status)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/statuses_create.html')

    def test_StatusCreateView_POST(self):
        response = self.client.post(
            '/statuses/create/',
            {
                'name': 'status_name_1',
            }
        )
        user = User.objects.get(username='test_5')
        self.client.force_login(user)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Status.objects.filter(name="status_name_1"))

    def test_StatusUpdateView_POST(self):
        status = Status.objects.get(name='test_status')
        response = self.client.get(
            reverse('update_status', args=(status.id,)), follow=True
        )
        self.assertEqual(response.status_code, 200)

        user = User.objects.get(username='test_5')
        self.client.force_login(user)
        response = self.client.post(
            '/statuses/1/update/',
            {'name': 'test_status_upd'}, kwargs={'id': status.id})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Status.objects.filter(name='test_status_upd'))

    def test_StatusesDeleteView_GET_and_POST(self):
        status = Status.objects.get(name='test_status')
        response = self.client.get(
            reverse('delete_label', args=(status.id,)), follow=True
        )
        self.assertEquals(response.status_code, 200)

        response = self.client.post(
            reverse('delete_status', kwargs={'id': status.id})
        )
        self.assertNotContains(response, 'delete_status', status_code=302)
        self.assertEqual(Status.objects.count(), 0)
