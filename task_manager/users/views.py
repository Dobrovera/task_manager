from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from task_manager.users.models import User
from django.views import View

def user(request):
    return HttpResponse("Пользователи")


@require_http_methods(["GET", "POST"])
def registration(request):
    return render(request, 'registration.html', context={})


class UserList(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users.html', context={
            'users': users,
        })


@require_http_methods(["GET", "POST"])
def users(request):
    return render(request, 'users.html', context={})