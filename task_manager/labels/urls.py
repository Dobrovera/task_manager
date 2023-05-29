from django.urls import path, include

from .views import *


urlpatterns = [
    path('', LabelsListView.as_view(), name='labels'),
    path('create/', LabelCreateView.as_view(), name='create_label'),
]
