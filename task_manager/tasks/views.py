from django.contrib import messages
from django.utils.translation import gettext
from django.views.generic.list import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from .forms import TaskCreateForm
from .filters import TaskFilter
from .models import Task


class TasksListView(ListView):
    model = Task
    template_name = 'tasks/tasks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        context['filter'] = TaskFilter(user_id, self.request.GET, queryset=self.get_queryset())
        return context


class TaskCreateView(View):

    def get(self, request, *args, **kwargs):
        form = TaskCreateForm()
        return render(request, 'tasks/task_create.html', context={
            "form": form
        })

    def post(self, request, *args, **kwargs):
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            if form['name'].value() not in Task.objects.values_list('name', flat=True).distinct():
                task = form.save(commit=False)
                task.author = request.user
                task.save()
                form.save_m2m()
                messages.success(request, gettext('Task created successfully'))
                return redirect('/tasks')
            else:
                text = gettext('A task with this name already exists')
                return render(request, 'tasks/task_create.html', context={'form': form, 'text': text})
        else:
            form = TaskCreateForm()
        return render(request, 'tasks/task_create.html', context={'form': form})


class TaskUpdateView(View):

    def get(self, request, *args, **kwargs):
        form = TaskCreateForm()
        return render(request, 'tasks/task_update.html', context={
            "form": form
        })

    def post(self, request, *args, **kwargs):
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            if form['name'].value() not in Task.objects.values_list('name', flat=True).distinct():
                task = form.save(commit=False)
                task.author = request.user
                task.save()
                messages.success(request, gettext('Task updated successfully'))
                return redirect('/tasks')
            else:
                text = gettext('A task with this name already exists')
                return render(request, 'tasks/task_update.html', context={'form': form, 'text': text})
        else:
            form = TaskCreateForm()
        return render(request, 'tasks/task_update.html', context={'form': form})


class TaskDeleteView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs['id'])
        if request.user.is_authenticated:
            if task.author_id == request.user.id:
                task = get_object_or_404(Task, id=kwargs['id'])
                return render(request, 'tasks/task_delete.html', context={
                "task": task
                })
            else:
                messages.error(request, gettext('Task can only be deleted by its author'))
                return redirect('/tasks')
        messages.error(request, gettext('You are not authorized! Please sign in.'))
        return redirect('/login')

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs['id'])
        if request.user.is_authenticated:
            if task.author_id == request.user.id:
                task.delete()
                messages.success(request, gettext('Task deleted successfully'))
                return redirect('/tasks')
            else:
                messages.error(request, gettext('Task can only be deleted by its author'))
                return redirect('/tasks')
        messages.error(request, gettext('Task can only be deleted by its author'))
        return redirect('/tasks')