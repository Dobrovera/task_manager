from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.translation import gettext
from django.views import View
from .models import Labels
from .forms import LabelsForm


class LabelsListView(View):

    def get(self, request, *args, **kwargs):
        labels = Labels.objects.all()
        return render(request, 'labels/labels.html', context={
            "labels": labels,
        })


class LabelCreateView(View):

    def get(self, request, *args, **kwargs):
        form = LabelsForm()
        return render(request, 'labels/label_create.html', context={'form': form})

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
