from django.urls import path, include

from .views import *


urlpatterns = [
    path('', LabelsListView.as_view(), name='labels'),
    path('create/', LabelCreateView.as_view(), name='create_label'),
    path('<int:id>/update', UpdateLabelView.as_view(), name='update_label'),
    path('<int:id>/delete', DeleteLabelView.as_view(), name='delete_label'),
]
