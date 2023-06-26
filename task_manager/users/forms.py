from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = _("Your password must "
                                               "be at least 3 characters long.")

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "password1",
        )


class UpdateUserForm(UserCreationForm):

    def __init__(self, user_id, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.user_id = user_id
        self.fields['password1'].help_text = _("Your password must "
                                               "be at least 3 characters long.")

    password = None

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
