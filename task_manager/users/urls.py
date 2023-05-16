from django.urls import path, include

from .views import *

urlpatterns = [
    path('', UserList.as_view()),
    path('create/', registration),
    path('<int:id>/update', Update.as_view())
]