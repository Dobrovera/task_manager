from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.utils.translation import gettext
from task_manager.tasks.models import Task
from .models import Status
from .forms import StatusesForm, UpdateStatusForm


class StatusesListView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            statuses = Status.objects.all().order_by('id')
            return render(request, 'statuses/statuses.html', context={
                "statuses": statuses,
            })
        messages.error(request, gettext(
            'You are not authorized! Please sign in.'
        ))
        return redirect('/login')


class StatusCreateView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = StatusesForm()
            return render(request, 'statuses/statuses_create.html',
                          context={
                              "form": form
                          })
        messages.error(request, gettext(
            'You are not authorized! Please sign in.'
        ))
        return redirect('/login')

    def post(self, request, *args, **kwargs):
        form = StatusesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, gettext('Status created successfully'))
            return redirect('/statuses')
        return render(request, 'statuses/statuses_create.html',
                      context={
                          "form": form
                      })


class StatusDeleteView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            status = get_object_or_404(Status, id=kwargs['id'])
            return render(request, 'statuses/status_delete.html', context={
                "status": status
            })
        messages.error(request, gettext(
            'You are not authorized! Please sign in.'
        ))
        return redirect('/login')

    def post(self, request, *args, **kwargs):
        status = get_object_or_404(Status, id=kwargs['id'])
        if status.id not in Task.objects.values_list('status_id', flat=True):
            status.delete()
            messages.success(request, gettext('Status deleted successfully'))
            return redirect('/statuses')
        else:
            messages.error(request, gettext(
                "Can't delete status because it's in use"
            ))
            return redirect('/statuses')


class StatusUpdateView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            status = get_object_or_404(Status, id=kwargs['id'])
            status_name = status.name
            form = UpdateStatusForm(status.id, {"name": status_name})
            return render(request, 'statuses/status_update.html', context={
                "status": status,
                "form": form,
            })
        messages.error(request, gettext(
            'You are not authorized! Please sign in.'
        ))
        return redirect('/login')

    def post(self, request, *args, **kwargs):
        status = get_object_or_404(Status, id=kwargs['id'])
        form = UpdateStatusForm(status.id, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, gettext('Status updated successfully'))
            return redirect('/statuses')
        else:
            return render(request, 'statuses/status_update.html', context={
                "form": form,
            })
