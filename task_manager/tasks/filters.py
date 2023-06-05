from django.forms import models
from django.forms.models import ModelForm
from .models import Task
import django_filters


class TaskFiter(django_filters.FilterSet):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']