from django.contrib.auth.models import User

from task_manager.labels.models import Label
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):

        self.client = Client()
        self.create_label = reverse('create_label')
        self.labels = reverse('labels')
        Label.objects.create(
            label_name='test_label'
        )
        User.objects.create(
            username='test_1',
            password='test_1',
            first_name='test_1',
            last_name='test_1',
        )

    def test_LabelsListView_GET(self):
        user = User.objects.get(username='test_1')
        self.client.force_login(user)
        response = self.client.get(self.labels)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/labels.html')

    def test_LabelCreateView_GET(self):
        response = self.client.get(self.labels)
        self.assertEquals(response.status_code, 302)

        user = User.objects.get(username='test_1')
        self.client.force_login(user)
        response = self.client.get(self.labels)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/labels.html')

    def test_LabelCreateView_POST(self):
        response = self.client.post(
            '/labels/create/',
            {
                'label_name': 'label_name_1',
            }
        )
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(username='test_1')
        self.client.force_login(user)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Label.objects.filter(label_name="label_name_1"))

    def test_LabelDeleteView_GET_and_POST(self):
        label = Label.objects.get(label_name='test_label')
        response = self.client.get(
            reverse('delete_label', args=(label.id,)), follow=True
        )
        self.assertEquals(response.status_code, 200)
        response = self.client.post(
            reverse('delete_label', kwargs={'id': label.id})
        )
        self.assertNotContains(response, 'label_delete', status_code=302)
        self.assertEqual(Label.objects.count(), 0)
