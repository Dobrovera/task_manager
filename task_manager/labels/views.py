from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext
from django.views import View
from task_manager.tasks.models import Task
from .models import Label
from .forms import LabelsForm, UpdateLabelForm


class LabelsListView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            labels = Label.objects.all().order_by('id')
            return render(request, 'labels/labels.html', context={
                "labels": labels,
            })
        messages.error(request, gettext(
            'You are not authorized! Please sign in.'
        ))
        return redirect('/login')


class LabelCreateView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = LabelsForm()
            return render(request, 'labels/label_create.html',
                          context={
                              "form": form
                          })
        messages.error(request, gettext(
            'You are not authorized! Please sign in.'
        ))
        return redirect('/login')

    def post(self, request, *args, **kwargs):
        form = LabelsForm(request.POST)
        if form.is_valid():
            if form['name'].value() not in \
                    Label.objects.values_list('name',
                                              flat=True).distinct():
                form.save()
                messages.success(request, gettext(
                    'Label created successfully'
                ))
                return redirect('/labels')
            else:
                return render(request, 'labels/label_create.html',
                              context={
                                  "form": form
                              })
        else:
            pass
        return render(request, 'labels/label_create.html',
                      context={
                          "form": form
                      })


class LabelUpdateView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            label = get_object_or_404(Label, id=kwargs['id'])
            label_name = label.name
            form = UpdateLabelForm(label.id, {"name": label_name})
            return render(request, 'labels/label_update.html', context={
                "label": label,
                "form": form,
            })
        messages.error(request, gettext(
            'You are not authorized! Please sign in.'
        ))
        return redirect('/login')

    def post(self, request, *args, **kwargs):
        label = get_object_or_404(Label, id=kwargs['id'])
        form = UpdateLabelForm(label.id, request.POST)
        if request.POST['name'] not in \
                Label.objects.all().values_list('name',
                                                flat=True):
            if form.is_valid():
                form.save()
                messages.success(request, gettext(
                    'Label updated successfully'
                ))
                return redirect('/labels')
            return redirect('/labels')
        else:
            return render(request, 'labels/label_update.html', context={
                "form": form,
            })


class LabelDeleteView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            label = get_object_or_404(Label, id=kwargs['id'])
            return render(request, 'labels/label_delete.html', context={
                "label": label
            })
        messages.error(request, gettext(
            'You are not authorized! Please sign in.'
        ))
        return redirect('/login')

    def post(self, request, *args, **kwargs):
        label = get_object_or_404(Label, id=kwargs['id'])
        if label.id not in Task.objects.values_list('labels', flat=True):
            label.delete()
            messages.success(request, gettext('Label deleted successfully'))
            return redirect('/labels')
        else:
            messages.error(request, gettext(
                "Can't delete label because it's in use"
            ))
            return redirect('/labels')
