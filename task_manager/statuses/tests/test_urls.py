from django.test import SimpleTestCase
from django.urls import reverse, resolve
from task_manager.statuses.views import StatusesListView, StatusCreateView, \
    StatusUpdateView, StatusDeleteView


class TestUrls(SimpleTestCase):

    def test_labels_url_valid(self):
        url = reverse('statuses')
        self.assertEquals(resolve(url).func.view_class, StatusesListView)

    def test_create_label_url_valid(self):
        url = reverse('create_status')
        self.assertEquals(resolve(url).func.view_class, StatusCreateView)

    def test_update_label_url_valid(self):
        url = reverse('update_status', args='1')
        self.assertEquals(resolve(url).func.view_class, StatusUpdateView)

    def test_delete_label_url_valid(self):
        url = reverse('delete_status', args='1')
        self.assertEquals(resolve(url).func.view_class, StatusDeleteView)
