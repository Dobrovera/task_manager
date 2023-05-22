from django.urls import path, include

from .views import *

urlpatterns = [
    path('', UserList.as_view()),
    path('create/', create_view),
    path('<int:id>/update', UpdateUser.as_view()),
    path('test/', test),
    path('testr/', TestView.as_view()),
]