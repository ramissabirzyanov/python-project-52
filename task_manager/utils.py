from django.forms import ValidationError
from django.contrib import messages
from django.shortcuts import redirect


class UniqueNameErrorMixin:

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if self._meta.model.objects.filter(name=name).exists():
            raise ValidationError(
                f'{self._meta.model._meta.verbose_name} с таким именем уже существует.')
        return name


class LoginRequiredMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request,
                           "Вы не авторизованы! Пожалуйста, выполните вход.")
            return redirect('login')
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class AuthenticationCheckMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        current_user = self.get_object()
        if request.user.username == current_user.username:
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(request,
                           "У вас нет прав для изменения другого пользователя")
            return redirect('users')
