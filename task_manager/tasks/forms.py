from django.core.exceptions import ValidationError
from django.utils.translation import gettext
from .models import Task
from django import forms


def validate_already_exist(value):
    if value in Task.objects.all().values_list('name', flat=True):
        raise ValidationError(
            gettext("A task with this name already exists"),
            params={"value": value},
        )


class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = (
            'name', 'description', 'status', 'executor', 'labels'
        )
