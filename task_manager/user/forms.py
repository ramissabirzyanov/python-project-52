from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class UserCreateForm(UserCreationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)
        self.fields['first_name'].label = _('First name')
        self.fields['last_name'].label = _('Last name')
        self.fields['username'].label = _('Username')
        self.fields['password'].label = _('Password')
        self.fields['password_confirmation'].label = _('Password confirmation')

    usable_password = None

    class Meta:
        model = get_user_model()
        fields = [
            'first_name', 'last_name', 'username', 'password1', 'password2'
            ]


class UserUpdateForm(UserCreateForm):

    class Meta:
        model = get_user_model()
        fields = [
            'first_name', 'last_name', 'username', 'password1', 'password2'
            ]

    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username
