from django.urls import path, include

from .views import *

urlpatterns = [
    path('', UserList.as_view(), name='users'),
    path('<int:id>/update', UpdateUserView.as_view(), name='update'),
    path('create/', SignUpView.as_view(), name='create'),
    path('<int:id>/delete', DeleteUser.as_view(), name='delete'),
]