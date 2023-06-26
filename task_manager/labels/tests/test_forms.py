from task_manager.users.models import User
from django.test import Client, TestCase
from django.urls import reverse
from task_manager.labels.forms import LabelsForm
from task_manager.labels.models import Label


class TestUserForms(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create(
            username='test_user',
            password='test_4',
            first_name='test_4',
            last_name='test_4',
        )

    def test_LabelsForm_valid_data(self):
        form = LabelsForm(data={
            "name": "label name",
        })

        self.assertTrue(form.is_valid())

    def test_UpdateLabelForm_valid_data(self):
        label = Label.objects.create(
            name='test_label'
        )
        response = self.client.post(
            reverse('update_label', kwargs={'id': label.id}),
            {'name': 'test_label_updated'})
        self.assertEqual(response.status_code, 302)
        label.refresh_from_db()
        self.assertEqual(label.name, 'test_label_updated')

        user = User.objects.get(username='test_user')
        self.client.force_login(user)
