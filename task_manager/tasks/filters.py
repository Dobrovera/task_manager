import django_filters
from django.utils.translation import gettext
from .models import Task


class TaskFilter(django_filters.FilterSet):

    label = django_filters.ModelChoiceFilter(label=gettext('Label'), queryset=Task.objects.all())

    class Meta:
        model = Task
        fields = ['status', 'executor', 'label']
