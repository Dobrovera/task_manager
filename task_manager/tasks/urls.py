from django.urls import path, include

from .views import *

urlpatterns = [
    path('', TasksListView.as_view(), name='tasks'),
    path('create/', TaskCreateView.as_view(), name='create_task'),
]