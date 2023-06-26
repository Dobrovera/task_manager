from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import gettext
from .models import Label


class LabelsForm(forms.ModelForm):

    class Meta:
        model = Label
        fields = (
            'name',
        )


class UpdateLabelForm(UserChangeForm):
    password = None

    def __init__(self, label_id, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.label_id = label_id

    name = forms.CharField(
        label=gettext("name"),
        strip=False,
        widget=forms.TextInput(),
        help_text='',
    )

    def save(self, commit=True):

        # написала кастомный save, так как стандартный save базового класса
        # вместо того, чтобы изменять юзера создавал нового юзера.

        label = Label.objects.get(id=self.label_id)
        label.name = self.cleaned_data.get('name')
        label.save()
        if hasattr(self, "save_m2m"):
            self.save_m2m()
        return label

    class Meta:
        model = Label
        fields = (
            'name',
        )
