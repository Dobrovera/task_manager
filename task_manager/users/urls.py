from django.urls import path
from .views import UserListView, UserUpdateView, SignUpView, UserDeleteView

urlpatterns = [
    path('', UserListView.as_view(), name='users'),
    path('<int:id>/update', UserUpdateView.as_view(), name='update'),
    path('create/', SignUpView.as_view(), name='create'),
    path('<int:id>/delete', UserDeleteView.as_view(), name='delete'),
]
