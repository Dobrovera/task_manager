from django.core.exceptions import ValidationError
from django.utils.translation import gettext
from .models import Task
from django import forms
from task_manager.labels.models import Label


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


class TaskUpdateForm(forms.ModelForm):

    def __init__(self, task_id, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.task_id = task_id

    def save(self, commit=True):

    # написала кастомный save, так как стандартный save базового клаccа
    # вместо того, чтобы изменять задачу создавал новую задачу.

        task = Task.objects.get(id=self.task_id)
        task.name = self.cleaned_data.get('name')
        task.description = self.cleaned_data.get('description')
        task.status = self.cleaned_data.get('status')
        task.executor = self.cleaned_data.get('executor')
        task.save()
        labels = self.cleaned_data.get('labels')
        label_id_list = []
        for label in labels:
            label_name = Label.objects.get(label_name=label)
            label_id = label_name.id
            label_id_list.append(label_id)
        task.labels.set(label_id_list)
        task.save()
        if hasattr(self, "save_m2m"):
            self.save_m2m()
        return task

    class Meta:
        model = Task
        fields = (
            'name', 'description', 'status', 'executor', 'labels'
        )
