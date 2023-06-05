from .models import Task
from django.shortcuts import render
from django.views import View


class TasksListView(View):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, 'tasks/tasks.html', context={
            "tasks": tasks,
        })