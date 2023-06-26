from django.urls import path
from .views import TasksListView, TaskCreateView, \
    TaskUpdateView, TaskDeleteView, TaskCardView


urlpatterns = [
    path('', TasksListView.as_view(), name='tasks'),
    path('create/', TaskCreateView.as_view(), name='create_task'),
    path('<int:id>/delete/', TaskDeleteView.as_view(), name='delete_task'),
    path('<int:id>/update/', TaskUpdateView.as_view(), name='update_task'),
    path('<int:id>/', TaskCardView.as_view(), name='task_card'),
]
