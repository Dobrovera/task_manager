from django.shortcuts import render, redirect
from django.views import View
from task_manager.statuses.models import Statuses
from task_manager.views import index


class StatusesList(View):

    def get(self, request, *args, **kwargs):
        statuses = Statuses.objects.all()
        return render(request, 'statuses/statuses.html', context={
            "statuses": statuses,
        })

def CreateStatus(request):
    return redirect(index)