from django.urls import path, include

from .views import *

urlpatterns = [
    path('', StatusesList.as_view(), name='statuses'),
    path('create/', CreateStatus.as_view(), name='create_status'),
    path('<int:id>/delete', DeleteStatus.as_view(), name='delete_status'),
]