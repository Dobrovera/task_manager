from django.contrib.auth.models import User
from django.utils.translation import gettext

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from django.db import models


class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='task_author_user',
                               verbose_name=gettext('Author'))
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name=gettext('Status'))
    executor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='task_executor_user',
                                 verbose_name=gettext('Executor'))
    labels = models.ManyToManyField(Label, verbose_name=gettext('Label'))
    description = models.TextField(verbose_name=gettext('Description'))
    name = models.CharField(max_length=250, verbose_name=gettext('Name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=gettext('created_at'))
