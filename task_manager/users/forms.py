from django.core.exceptions import ValidationError
from django.utils.translation import gettext
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django import forms


def username_already_exist(value):
    if value in User.objects.all().values_list('username', flat=True):
        raise ValidationError(
            gettext("User with the same name already exists."),
            params={"value": value},
        )


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'Ваш пароль должен ' \
                                             'содержать как минимум 3 символа.'

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "password1",
        )


class UpdateUserForm(UserCreationForm):
    password = None

    username = forms.CharField(
        label=_("Username"),
        widget=forms.TextInput(),
        strip=False,
        help_text=_("Obligatory field. No more than 150 characters. "
                    "Letters, numbers and symbols @/./+/-/_ only."),
    )

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(),
        help_text=_("Your password must be at least 3 characters long."),
    )

    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    def __init__(self, user_id, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.user_id = user_id

    def save(self, commit=True):

        # написала кастомный save, так как стандартный save базового класса
        # UserChangeForm вместо того, чтобы изменять юзера
        # создавал нового юзера

        user = User.objects.get(id=self.user_id)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.username = self.cleaned_data.get('username')
        user.set_password(self.cleaned_data["password1"])
        user.save()
        if hasattr(self, "save_m2m"):
            self.save_m2m()
        return user

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username"
        )
