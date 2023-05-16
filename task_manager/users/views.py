from django.shortcuts import render, get_object_or_404
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

class Update(View):

    def get(self, request, *args, **kwargs):
        users = get_object_or_404(User, id=kwargs['id'])
        return render(request, 'update.html', context={
            'users': users,
        })