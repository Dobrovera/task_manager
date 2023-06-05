from django.contrib.auth.models import User
from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from django.db import models


class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='task_author_user')
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    executor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='task_executor_user')
    labels = models.ManyToManyField(Label)
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)