from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Status
from django.utils.translation import gettext


class StatusesForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = (
            'name',
        )


class UpdateStatusForm(UserChangeForm):

    password = None

    def __init__(self, status_id, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.status_id = status_id

    name = forms.CharField(
        label=gettext("name"),
        strip=False,
        widget=forms.TextInput(),
        help_text='',
    )

    def save(self, commit=True):

        status = Status.objects.get(id=self.status_id)
        status.name = self.cleaned_data.get('name')
        status.save()
        if hasattr(self, "save_m2m"):
            self.save_m2m()
        return status

    class Meta:
        model = Status
        fields = (
            'name',
        )
