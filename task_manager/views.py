from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html', context={})


@login_required
def logout_view(request):
    logout(request)
    return redirect(index)
