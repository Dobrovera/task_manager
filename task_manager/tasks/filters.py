from django.core.exceptions import ValidationError
from django.utils.translation import gettext
from .models import Task
import django_filters
from django import forms
from ckeditor.fields import RichTextField


def validate_already_exist(value):
    if value in Task.objects.all().values_list('name', flat=True):
        raise ValidationError(
            gettext("A task with this name already exists"),
            params={"value": value},
        )


class TaskFiter(django_filters.FilterSet):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']