from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):

        self.tasks_url = reverse('tasks')
        self.task_create_url = reverse('create_task')
        self.task_update_url = reverse('update_task', kwargs={"id": 5})
        self.task_delete_url = reverse('delete_task', kwargs={"id": 4})

    def test_TasksListView_GET_for_NOT_auth_user(self):
        response = self.client.get(self.tasks_url)
        self.assertEquals(response.status_code, 302)

    def test_TaskCreateView_GET_for_NOT_auth_user(self):
        response = self.client.get(self.task_create_url)
        self.assertEquals(response.status_code, 302)
