from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import get_object_or_404


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'Ваш пароль должен содержать как минимум 3 символа.'
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "password1",
        )


class UpdateUserForm(UserCreationForm):

    def __init__(self, request, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'Ваш пароль должен содержать как минимум 3 символа.'

        if request == "GET":
            self.fields['first_name'] = forms.CharField(initial=args[0]['first_name'])
            self.fields['last_name'] = forms.CharField(initial=args[0]['last_name'])
            self.fields['username'] = forms.CharField(initial=args[0]['username'])
        else:
            self.fields['first_name'] = forms.CharField(initial=request['first_name'])
            self.fields['last_name'] = forms.CharField(initial=request['last_name'])
            self.fields['username'] = forms.CharField(initial=request['username'])

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "password1",
        )