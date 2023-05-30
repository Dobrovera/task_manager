from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext
from django.views import View
from .models import Labels
from .forms import LabelsForm, UpdateLabelForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class LabelsListView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            labels = Labels.objects.all()
            return render(request, 'labels/labels.html', context={
                "labels": labels,
            })
        messages.error(request, gettext('You are not authorized! Please sign in.'))
        return redirect('/login')


class LabelCreateView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = LabelsForm()
            return render(request, 'labels/label_create.html', context={'form': form})
        messages.error(request, gettext('You are not authorized! Please sign in.'))
        return redirect('/login')


    def post(self, request, *args, **kwargs):
        form = LabelsForm(request.POST)
        if form.is_valid():
            if form['label_name'].value() not in Labels.objects.values_list('label_name', flat=True).distinct():
                form.save()
                messages.success(request, gettext('Label created successfully'))
                return redirect('/labels')
            else:
                return render(request, 'labels/label_create.html', context={'form': form})
        else:
            form = LabelsForm()
        return render(request, 'labels/label_create.html', context={'form': form})


class UpdateLabelView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            label = get_object_or_404(Labels, id=kwargs['id'])
            label_name = label.label_name
            form = UpdateLabelForm(label.id, {"label_name": label_name})
            return render(request, 'labels/label_update.html', context={
                "label": label,
                "form": form,
            })
        messages.error(request, gettext('You are not authorized! Please sign in.'))
        return redirect('/login')

    def post(self, request, *args, **kwargs):
        label = get_object_or_404(Labels, id=kwargs['id'])
        form = UpdateLabelForm(label.id, request.POST)
        if request.POST['label_name'] not in Labels.objects.all().values_list('label_name', flat=True):
            if form.is_valid():
                form.save()
                messages.success(request, gettext('Label updated successfully'))
                return redirect('/labels')
            return redirect('/labels')
        else:
            return render(request, 'labels/label_update.html', context={
                "form": form,
            })


class DeleteLabelView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            label = get_object_or_404(Labels, id=kwargs['id'])
            return render(request, 'labels/label_delete.html', context={
                "label": label
            })
        messages.error(request, gettext('You are not authorized! Please sign in.'))
        return redirect('/login')

    def post(self, request, *args, **kwargs):
        label = get_object_or_404(Labels, id=kwargs['id'])
        label.delete()
        messages.success(request, gettext('Label deleted successfully'))
        return redirect('/labels')
