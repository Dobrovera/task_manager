"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from task_manager import views
from task_manager.users.views import LoginView, logout_view

urlpatterns = [
    path('', views.inde),
    path('admin/', admin.site.urls),
    path('users/', include('task_manager.users.urls'), name='users'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('statuses/', include('task_manager.statuses.urls'), name='statuses'),
    path('labels/', include('task_manager.labels.urls'), name='labels'),
    path('tasks/', include('task_manager.tasks.urls'), name='tasks')
]
