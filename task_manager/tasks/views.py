from .models import Task
from django.shortcuts import render
from django.views import View
from .filters import TaskFiter

class TasksListView(View):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, 'tasks/tasks.html', context={
            "tasks": tasks,
        })


class TaskCreateView(View):

    def get(self, request, *args, **kwargs):
        task_filter = TaskFiter()
        return render(request, 'tasks/task_create.html', context={
            "task_filter": task_filter
        })