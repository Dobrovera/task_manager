from django.urls import path, include

from .views import *

urlpatterns = [
    path('', UserList.as_view()),
    path('<int:id>/update', UpdateUser.as_view()),
    path('create/', SignUpView.as_view()),
]