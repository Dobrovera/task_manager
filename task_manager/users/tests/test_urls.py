from django.test import SimpleTestCase
from django.urls import reverse, resolve
from task_manager.users.views import UserListView, SignUpView, \
    UserUpdateView, UserDeleteView


class TestUrls(SimpleTestCase):

    def test_users_url_valid(self):
        url = reverse('users')
        self.assertEquals(resolve(url).func.view_class, UserListView)

    def test_create_url_valid(self):
        url = reverse('create')
        self.assertEquals(resolve(url).func.view_class, SignUpView)

    def test_update_url_valid(self):
        url = reverse('update', args='1')
        self.assertEquals(resolve(url).func.view_class, UserUpdateView)

    def test_delete_url_valid(self):
        url = reverse('delete', args='1')
        self.assertEquals(resolve(url).func.view_class, UserDeleteView)
