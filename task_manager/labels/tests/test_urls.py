from django.test import SimpleTestCase
from django.urls import reverse, resolve
from task_manager.labels.views import LabelsListView, LabelCreateView, \
    LabelDeleteView, LabelUpdateView


class TestUrls(SimpleTestCase):

    def test_labels_url_valid(self):
        url = reverse('labels')
        self.assertEquals(resolve(url).func.view_class, LabelsListView)

    def test_create_label_url_valid(self):
        url = reverse('create_label')
        self.assertEquals(resolve(url).func.view_class, LabelCreateView)

    def test_update_label_url_valid(self):
        url = reverse('update_label', args='1')
        self.assertEquals(resolve(url).func.view_class, LabelUpdateView)

    def test_delete_label_url_valid(self):
        url = reverse('delete_label', args='1')
        self.assertEquals(resolve(url).func.view_class, LabelDeleteView)
