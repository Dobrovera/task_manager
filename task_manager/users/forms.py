from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control is-valid',
            'id': 'id_first_name',
            'placeholder': 'Имя',
            'required':'',
            'value': '',
            'name': 'first_name'
        })
        self.fields['last_name'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control is-valid',
            'id': 'id_last_name',
            'placeholder': 'Фамилия',
            'required': '',
            'value': '',
            'name': 'last_name'
        })
        self.fields['username'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control is-valid',
            'id': 'id_username',
            'placeholder': 'Имя пользователя',
            'required': '',
            'value': '',
            'name': 'username'
        })
        self.fields['password'].widget.attrs.update({
            'type': 'password',
            'class': 'form-control is-valid',
            'id': 'id_password',
            'placeholder': 'Пароль',
            'required': '',
            'value': '',
            'name': 'password'
        })
        self.fields['password2'].widget.attrs.update({
            'type': 'password',
            'class': 'form-control is-valid',
            'id': 'id_password2',
            'placeholder': 'Подтверждение пароля',
            'required': '',
            'value': '',
            'name': 'password2'
        })

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'password2']


class TestForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
        )