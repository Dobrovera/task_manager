from django.urls import path, include

from .views import *

urlpatterns = [
    path('', UserList.as_view()),
    path('create/', registration),
]