from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.test import Client
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.tasks_url = reverse('tasks')
        self.task_create_url = reverse('create_task')
        self.author = User.objects.create(
            username='test_author',
            password='test_author',
            first_name='test_author',
            last_name='test_author',
        )
        self.executor = User.objects.create(
            username='test_executor',
            password='test_executor',
            first_name='test_executor',
            last_name='test_executor',
        )
        self.status = Status.objects.create(
            status_name='test_status'
        )
        self.client.login(username='test_author', password='test_author')
        Task.objects.create(
            name='test_task_one',
            author_id=self.author.id,
            description='test_task_one_description',
            status_id=self.status.id,
            executor_id=self.executor.id,
        )

    def test_TasksListView_GET(self):
        response = self.client.get(self.tasks_url)
        self.assertEquals(response.status_code, 302)

        user = User.objects.get(username='test_author')
        self.client.force_login(user)
        response = self.client.get(self.task_create_url)
        self.assertEquals(response.status_code, 200)

    def test_TaskCreateView_GET(self):
        response = self.client.get(self.task_create_url)
        self.assertEquals(response.status_code, 302)

        user = User.objects.get(username='test_author')
        self.client.force_login(user)
        response = self.client.get(self.task_create_url)
        self.assertEquals(response.status_code, 200)

    def test_TaskCreateView_POST(self):
        user = User.objects.get(username='test_author')
        self.client.force_login(user)
        response = self.client.post(
            reverse('create_task'),
            {
                'name': "test_task",
                'author': self.author,
                'description': 'some_description',
                'status': self.status.id,
                'executor': self.executor.id,
            }
        )
        self.assertEqual(response.status_code, 302)
        task = Task.objects.get(name='test_task')
        self.assertEqual(task.name, "test_task")
        self.assertEqual(task.author, self.author)
        self.assertEqual(task.description, "some_description")
        self.assertEqual(task.status.id, self.status.id)
        self.assertEqual(task.executor.id, self.executor.id)
