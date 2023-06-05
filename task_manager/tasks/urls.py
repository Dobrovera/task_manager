from django.urls import path, include

from .views import *

urlpatterns = [
    path('', TasksListView.as_view(), name='tasks'),
]