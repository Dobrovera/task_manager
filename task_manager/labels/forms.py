from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext

from .models import Labels


def validate_already_exist(value):
    if value in Labels.objects.all().values_list('label_name', flat=True):
        raise ValidationError(
            gettext("A label with this name already exists"),
            params={"value": value},
        )


class LabelsForm(forms.ModelForm):


    label_name = forms.CharField(
        label=gettext("label_name"),
        strip=False,
        widget=forms.TextInput(),
        help_text='',
        validators=[validate_already_exist]
    )

    class Meta:
        model = Labels
        fields = (
            'label_name',
        )



class UpdateLabelForm(UserChangeForm):
    password = None

    def __init__(self, label_id, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.label_id = label_id

    label_name = forms.CharField(
        label=gettext("label_name"),
        strip=False,
        widget=forms.TextInput(),
        help_text='',
        validators=[validate_already_exist]
    )

    def save(self, commit=True):

    # написала кастомный save, так как стандартный save базового класса
    # вместо того, чтобы изменять юзера создавал нового юзера.

        label = Labels.objects.get(id=self.label_id)
        label.label_name = self.cleaned_data.get('label_name')
        label.save()
        if hasattr(self, "save_m2m"):
            self.save_m2m()
        return label

    class Meta:
        model = Labels
        fields = (
            'label_name',
        )