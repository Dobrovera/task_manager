from django.shortcuts import render
from django.http import HttpResponse


def user(request):
    return HttpResponse("Пользователи")


def registration(request):
    return render(request, 'registration.html', context={})
