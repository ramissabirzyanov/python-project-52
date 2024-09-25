from django.shortcuts import redirect
from django.urls import reverse_lazy
from task_manager.user.models import User
from task_manager.task.models import Task
from .forms import UserCreateForm, UserUpdateForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from task_manager.utils import CurrentUserCheckMixin
from django.db.models import Q


class UsersListView(ListView):
    model = User
    template_name = 'user/users.html'
    queryset = User.objects.all().order_by('id')


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = 'user/user_create.html'
    success_url = reverse_lazy('login')
    success_message = 'Пользователь успешно зарегистрирован'


class UserUpdateView(CurrentUserCheckMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user/user_update.html'
    success_url = reverse_lazy('users')
    success_message = 'Пользователь успешно изменен'


class UserDeleteView(CurrentUserCheckMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'user/user_delete.html'
    success_url = reverse_lazy('main_page')
    success_message = 'Пользователь успешно удален'

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        if Task.objects.filter(Q(author_id=user.id) | Q(executor_id=user.id)):
            messages.error(
                request,
                'Невозможно удалить пользователя, потому что он используется')
            return redirect('users')
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
