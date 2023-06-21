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
            id=10,
            name='test_task_one',
            author_id=self.author.id,
            description='test_task_one_description',
            status_id=self.status.id,
            executor_id=self.executor.id,
        )
        Status.objects.create(
            status_name='test_status_name'
        )

    def test_TasksListView_GET(self):
        response = self.client.get(self.tasks_url)
        self.assertEquals(response.status_code, 302)

        user = User.objects.get(username='test_author')
        self.client.force_login(user)
        response = self.client.get(self.tasks_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            template_name='tasks/tasks.html'
        )

    def test_TaskCreateView_GET_and_POST(self):
        response = self.client.get(self.task_create_url)
        self.assertEquals(response.status_code, 302)

        user = User.objects.get(username='test_author')
        self.client.force_login(user)
        response = self.client.get(self.task_create_url)
        self.assertEquals(response.status_code, 200)

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

    def test_TaskUpdateView_GET_and_POST(self):
        user = User.objects.get(username='test_author')
        self.client.force_login(user)
        task = Task.objects.get(name='test_task_one')
        response = self.client.post(
            '/tasks/10/update',
            {
                'name': 'test_task_upd',
                'author': self.author,
                'description': 'test_task_upd_description',
                'status': self.status.id,
                'executor': self.executor.id,
            }, kwargs={'id': task.id}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(name="test_task_upd"))

        response = self.client.post(
            '/tasks/10/update',
            {
                'name': 'test_task_upd',
                'author': self.author,
                'description': 'test_task_upd_description',
                'status_invalid': self.status.id,
                'executor_invalid': self.executor.id,
            }, kwargs={'id': task.id}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
                    response,
                    template_name='tasks/task_update.html'
                )

    def test_TaskDeleteView_GET_and_POST(self):
        task = Task.objects.get(name='test_task_one')
        response = self.client.get(
            reverse('delete_task', args=(task.id,)), follow=True
        )
        self.assertEquals(response.status_code, 200)

        user = User.objects.get(username='test_author')
        self.client.force_login(user)
        response = self.client.post(
            reverse('delete_task', kwargs={'id': task.id})
        )
        self.assertNotContains(response, 'delete_task', status_code=302)
        self.assertEqual(Task.objects.count(), 0)
