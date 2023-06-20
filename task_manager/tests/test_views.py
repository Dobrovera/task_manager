from django.test import TestCase
from django.urls import reverse, resolve
from task_manager.views import index


class TestViews(TestCase):

    def test_indexView(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, index)
