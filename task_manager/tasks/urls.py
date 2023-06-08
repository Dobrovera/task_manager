from django.urls import path, include

from .views import *

urlpatterns = [
    path('', TasksListView.as_view(), name='tasks'),
    path('create/', TaskCreateView.as_view(), name='create_task'),
    path('<int:id>/delete', TaskDeleteView.as_view(), name='delete_task'),
    path('<int:id>/update', TaskUpdateView.as_view(), name='update_task'),
]