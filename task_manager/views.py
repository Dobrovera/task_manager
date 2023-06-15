from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html', context={})


@login_required
def logout_view(request):
    logout(request)
    return redirect(index)

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    a = None
    a.hello() # Creating an error with an invalid line of code
    return HttpResponse("Hello, world. You're at the pollapp index.")