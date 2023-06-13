from django.test import SimpleTestCase
from django.urls import reverse, resolve
from task_manager.users.views import LoginView


class TestUrls(SimpleTestCase):

    def test_login_url(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, LoginView)
