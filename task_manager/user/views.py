from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse, reverse_lazy
from task_manager.user.models import User
from .forms import UserCreateForm, UserUpdateForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

class AuthenticationCheckMixin:
    def dispatch(self, request, *args, **kwargs):
        current_user = self.get_object()
        if request.user.is_authenticated == False:
            messages.error(request, "Вы не авторизованы! Пожалуйста, выполните вход.")
            return redirect('login')
        if request.user.username == current_user.username:
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(request, "У вас нет прав для изменения другого пользователя.")
            return redirect('users')


class UsersListView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'user/users.html', context={'users': users})

    
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
