from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.core import validators
from django.core.exceptions import ValidationError

from .models import Statuses
from django.utils.translation import gettext



class StatusesForm(forms.ModelForm):

    class Meta:
        model = Statuses
        fields = (
            'status_name',
        )

def valudate_already_exist(value):
    if value in Statuses.objects.all().values_list('status_name', flat=True):
        raise ValidationError(
            gettext("A task status with this name already exists"),
            params={"value": value},
        )

class UpdateStatusForm(UserChangeForm):
    password = None

    def __init__(self, status_id, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.status_id = status_id

    status_name = forms.CharField(
        label=gettext("status_name"),
        strip=False,
        widget=forms.TextInput(),
        help_text='',
        validators=[valudate_already_exist]
    )

    def save(self, commit=True):

    # написала кастомный save, так как стандартный save базового класса
    # вместо того, чтобы изменять юзера создавал нового юзера.

        status = Statuses.objects.get(id=self.status_id)
        status.status_name = self.cleaned_data.get('status_name')
        status.save()
        if hasattr(self, "save_m2m"):
            self.save_m2m()
        return status

    class Meta:
        model = Statuses
        fields = (
            'status_name',
        )