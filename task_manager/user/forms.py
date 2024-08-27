from task_manager.user.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    usable_password = None
    class Meta:
        model = User
        help_texts = {
            'password': 'Ваш пароль должен содержать как минимум 3 символа.',
        }
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
