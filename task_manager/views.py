from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', context={})


@login_required
def logout_view(request):
    logout(request)
    return redirect(index)


def inde(request):
    a = None
    a.hello()  # Creating an error with an invalid line of code
    return HttpResponse("Hello, world. You're at the pollapp index.")
