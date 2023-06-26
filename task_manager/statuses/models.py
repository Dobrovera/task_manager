from django.db import models
from django.utils.translation import gettext


class Status(models.Model):
    name = models.CharField(
        max_length=250,
        unique=True,
        verbose_name=gettext('Name'),
        error_messages={
            "unique": gettext("%(model_name)s with this name already exists.")
        })
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = gettext('Status')
