from django.urls import path
from .views import *

urlpatterns = [
    path('', StatusesListView.as_view(), name='statuses'),
    path('create/', StatusCreateView.as_view(), name='create_status'),
    path('<int:id>/delete', StatusDeleteView.as_view(), name='delete_status'),
    path('<int:id>/update', StatusUpdateView.as_view(), name='update_status'),
]