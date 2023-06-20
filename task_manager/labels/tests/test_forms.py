from django.test import SimpleTestCase
from task_manager.labels.forms import LabelsForm


class TestUserForms(SimpleTestCase):
    databases = '__all__'

    def test_LabelsForm_valid_data(self):
        form = LabelsForm(data={
            "label_name": "label name",
        })

        self.assertTrue(form.is_valid())
