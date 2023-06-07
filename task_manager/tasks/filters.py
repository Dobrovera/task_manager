import django_filters
from django.utils.translation import gettext
from task_manager.labels.models import Label
from .models import Task
from django import forms


class TaskFilter(django_filters.FilterSet):

    labels = django_filters.ModelChoiceFilter(
        label=gettext('Label'),
        queryset=Label.objects.all()
    )

    author = django_filters.BooleanFilter(
        label=gettext('Only self tasks'),
        widget=forms.CheckboxInput,
        method='get_own_tasks',
        field_name='only_self_tasks'
    )

    def __init__(self, user_id, *args, **kwargs):
        super(django_filters.FilterSet, self).__init__(*args, **kwargs)
        self.user_id = user_id

    def get_own_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.user_id)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor']
