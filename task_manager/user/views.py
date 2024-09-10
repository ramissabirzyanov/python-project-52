from django.shortcuts import redirect
from django.urls import reverse_lazy
from task_manager.user.models import User
from .forms import UserCreateForm, UserUpdateForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class AuthenticationCheckMixin:
    def dispatch(self, request, *args, **kwargs):
        current_user = self.get_object()
        if not request.user.is_authenticated:
            messages.error(request,
                           "Вы не авторизованы! Пожалуйста, выполните вход.")
            return redirect('login')
        if request.user.username == current_user.username:
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(request,
                           "У вас нет прав для изменения другого пользователя")
            return redirect('users')


class UsersListView(ListView):
    model = User
    template_name = 'user/users.html'
    queryset = User.objects.all().order_by('id')


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = 'user/user_create.html'
    success_url = reverse_lazy('login')
    success_message = 'Пользователь успешно зарегистрирован'


class UserUpdateView(AuthenticationCheckMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user/user_update.html'
    success_url = reverse_lazy('users')
    login_url = 'login'
    success_message = 'Пользователь успешно изменен'


class UserDeleteView(AuthenticationCheckMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'user/user_delete.html'
    success_url = reverse_lazy('main_page')
    success_message = 'Пользователь успешно удален'
