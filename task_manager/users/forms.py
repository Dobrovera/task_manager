from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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