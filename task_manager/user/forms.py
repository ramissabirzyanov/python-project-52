from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import ValidationError


class UserCreateForm(UserCreationForm):
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
        current_user = self._meta.model.objects\
            .filter(username=username)\
            .first()
        if current_user and current_user.username != username:
            raise ValidationError(
                'Пользователь с таким именем уже существует.')
        return username
