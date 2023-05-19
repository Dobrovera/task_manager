from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.views import View
from django.contrib import messages
from django.utils.translation import gettext_lazy
from django.contrib.auth import authenticate, login, logout
from task_manager.views import index


class UserList(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/users.html', context={
            'users': users,
        })


class UpdateUser(View):

    def get(self, request, *args, **kwargs):
        users = get_object_or_404(User, id=kwargs['id'])
        return render(request, 'update.html', context={
            'users': users,
        })


@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Вы залогинены')
            print('ЗАЛОГИНЕНО')
            return render(request, 'index.html')
        else:
            messages.warning(request, 'Пожалуйста, введите правильные имя пользователя и пароль.'
                                      'Оба поля могут быть чувствительны к регистру.')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

@require_http_methods(["GET", "POST"])
def create_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'login.html')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password
                )
                user.set_password(password)
                user.save()
                return redirect(login_view)
    else:
        return render(request, 'users/create.html')


@require_http_methods(["GET", "POST"])
def logout_view(request):
    logout(request)
    return redirect(index)