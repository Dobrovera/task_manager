from django import forms
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
