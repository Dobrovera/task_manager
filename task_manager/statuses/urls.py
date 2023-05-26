from django.urls import path, include

from .views import *

urlpatterns = [
    path('', StatusesList.as_view(), name='statuses'),
    path('create/', CreateStatus, name='create_status')
]