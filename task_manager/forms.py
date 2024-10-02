from task_manager.user.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ["username", "password"]
