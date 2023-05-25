from django.contrib.auth.forms import UserCreationForm, UserChangeForm, BaseUserCreationForm
from django.utils.translation import gettext_lazy as _
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


class UpdateUserForm(UserChangeForm):
    password = None

    username = forms.CharField(
        label=_("Username"),
        widget=forms.TextInput(),
        strip=False,
        help_text="Хуй"
    )
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(),
        help_text='Ваш пароль должен содержать как минимум 3 символа.',
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    def __init__(self, user_id, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.user_id = user_id
        # self.fields['password'].help_text = 'Ваш пароль должен содержать как минимум 3 символа.'

        # self.fields['first_name'] = forms.CharField(initial=args[0]['first_name'])
        # self.fields['last_name'] = forms.CharField(initial=args[0]['last_name'])
        # self.fields['username'] = forms.CharField(initial=args[0]['username'])

    def save(self, commit=True):
        user = User.objects.get(id=self.user_id)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.username = self.cleaned_data.get('username')
        user.password = self.cleaned_data.get('password1')
        user.save()
        return user
        # print(user)
        # user: User = super(UserChangeForm, self).save(commit=False)
        # print(user)
        # user.set_password(self.cleaned_data["password1"])
        # user.username = self.cleaned_data['username']
        # if commit:
        #     user.save()
        #     if hasattr(self, "save_m2m"):
        #         self.save_m2m()
        # return user

    # def is_valid(self):
    #     super().is_valid()
    #     return True

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            # "username",
            # "password",
        )